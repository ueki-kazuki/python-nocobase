import json
from typing import Optional, List, Any

import requests

from ..api import NocoBaseAPI
from ..exceptions import NocoBaseAPIError, NocoBaseCollectionNotFoundError
from ..nocobase import AuthToken, NocoBaseClient


class NocoBaseRequestsClient:
    def __init__(self, auth_token: AuthToken, base_uri: str):
        self.__session = requests.Session()
        self.__session.headers.update(
            auth_token.get_header(),
        )
        self.__session.headers.update({"Content-Type": "application/json"})
        self.__api_info = NocoBaseAPI(base_uri)

    def _request(self, method: str, url: str, *args, **kwargs):
        response = self.__session.request(method, url, *args, **kwargs)
        response_json = None
        try:
            response.raise_for_status()
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            ...
        except requests.exceptions.HTTPError as http_error:
            raise NocoBaseAPIError(
                message=str(http_error),
                status_code=http_error.response.status_code,
                response_json=response_json,
                response_text=response.text,
            )

        return response

    def collections(self):
        return Collections(self)

    def collection(self, name: str):
        collections = self.list_collections()
        for c in collections:
            if c["name"] == name:
                return Collection(self, c)
        raise NocoBaseCollectionNotFoundError(f"Collection {name} is not found")

    def list_collections(self) -> List[dict]:
        resp = self._request("GET", self.__api_info.get_collections_uri()).json()
        return resp["data"] if "data" in resp else resp

    def list(self, collection: str, params: Optional[dict]) -> Any:
        while True:
            resp = self._request(
                "GET", self.__api_info.get_collection_uri_for(collection), params=params
            ).json()
            for d in resp["data"]:
                yield d

            page = resp["meta"]["page"] or 1
            total = resp["meta"]["totalPage"]
            if page == total:
                break
            params = params or {}
            params["page"] = page + 1
        

    def get(self, collection: str, params: dict) -> dict:
        return self._request(
            "GET",
            self.__api_info.get_collection_uri_for(collection, "get"),
            params=params,
        ).json()

    def create(self, collection: str, params: dict, body: dict) -> dict:
        return self._request(
            "POST",
            self.__api_info.get_collection_uri_for(collection, "create"),
            params=params,
            json=body,
        ).json()

    def update(self, collection: str, params: dict, body: dict) -> dict:
        return self._request(
            "POST",
            self.__api_info.get_collection_uri_for(collection, "update"),
            params=params,
            json=body,
        ).json()


class Collection(NocoBaseClient):
    def __init__(self, requester: NocoBaseRequestsClient, data: dict) -> None:
        self.requester = requester
        self.data = data
        self.name = data["name"]

    def __getitem__(self, __name: str):
        return self.data[__name]

    def list(
        self,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        filter: Optional[dict] = None,
        sort: List[str] = [],
        fields: List[str] = [],
        appends: List[str] = [],
        excepts: List[str] = [],
    ) -> List[dict]:
        params = {}
        if page:
            params["page"] = page
        if page_size:
            params["pageSize"] = page_size
        if filter:
            params["filter"] = json.dumps(filter)
        params["sort"] = sort
        params["fields"] = fields
        params["appends"] = appends
        params["except"] = excepts
        return self.requester.list(self.name, params)

    def get(
        self,
        id: Optional[int] = None,
        filter: Optional[dict] = None,
        sort: List[str] = [],
        fields: List[str] = [],
        appends: List[str] = [],
        excepts: List[str] = [],
    ) -> dict:
        """
        :param list[str] sort: items by fields, example: -field1,-field2,field3

        """
        params = {}
        if id:
            params["filterByTk"] = id
        if filter:
            params["filter"] = json.dumps(filter)
        params["sort"] = sort
        params["fields"] = fields
        params["appends"] = appends
        params["except"] = excepts
        return self.requester.get(self.name, params)

    def create(
        self,
        body: dict,
        whitelist: List[str] = [],
        blacklist: List[str] = [],
    ) -> dict:
        params = {}
        params["whitelist"] = whitelist
        params["blacklist"] = blacklist
        return self.requester.create(self.name, params, body)

    def update(
        self,
        body: dict,
        id: Optional[int] = None,
        filter: Optional[dict] = None,
        whitelist: List[str] = [],
        blacklist: List[str] = [],
    ) -> dict:
        params = {}
        if id:
            params["filterByTk"] = id
        if filter:
            params["filter"] = json.dumps(filter)
        params["whitelist"] = whitelist
        params["blacklist"] = blacklist
        return self.requester.update(self.name, params, body)


class Collections:
    def __init__(self, requester) -> None:
        self.requester = requester

    def list(self) -> list[Collection]:
        collections = []
        for raw in self.requester.list_collections():
            collections.append(Collection(self.requester, raw))
        return collections

    def get(self, name):
        collections = self.list()
        for c in collections:
            if c["name"] == name:
                return c

    # following methods are not implemented yet
    def create(self):
        pass

    def update(self):
        pass

    def destroy(self):
        pass

    def move(self):
        pass

    def set_fields(self):
        pass


class CollectionsFields(NocoBaseClient):
    def move(self):
        pass


class CollectionCategories(NocoBaseClient):
    def move(self):
        pass


class DbViews:
    def get(self):
        pass

    def list(self):
        pass

    def query(self):
        pass
