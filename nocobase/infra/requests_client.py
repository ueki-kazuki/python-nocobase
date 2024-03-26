from typing import Optional
from ..nocobase import AuthToken
from ..api import NocobaseAPI
from ..exceptions import NocobaseAPIError

import requests

class NocobaseRequestsClient:
    def __init__(self, auth_token: AuthToken, base_uri: str):
        self.__session = requests.Session()
        self.__session.headers.update(
            auth_token.get_header(),
        )
        self.__session.headers.update({"Content-Type": "application/json"})
        self.__api_info = NocobaseAPI(base_uri)

    def _request(self, method: str, url: str, *args, **kwargs):
        response = self.__session.request(method, url, *args, **kwargs)
        response_json = None
        try:
            response.raise_for_status()
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            ...
        except requests.exceptions.HTTPError as http_error:
            raise NocobaseAPIError(
                message=str(http_error),
                status_code=http_error.response.status_code,
                response_json=response_json,
                response_text=response.text
            )

        return response

    def collections(self) -> dict:
        return self._request(
            "GET", self.__api_info.get_collections_uri()
        ).json()

    def list(self, collection: str, params: Optional[dict]) -> dict:
        return self._request(
            "GET", self.__api_info.get_collection_uri_for(collection), params=params
        ).json()

    def get(self, collection: str, params: dict) -> dict:
        return self._request(
            "GET", self.__api_info.get_collection_uri_for(collection, "get"), params=params
        ).json()
    
    def create(self, collection: str, params: dict, body: dict) -> dict:
        return self._request(
            "POST", self.__api_info.get_collection_uri_for(collection, "create"), params=params, json=body
        ).json()
    
    def update(self, collection: str, params: dict, body: dict) -> dict:
        return self._request(
            "POST", self.__api_info.get_collection_uri_for(collection, "update"), params=params, json=body
        ).json()


class Collection:
    def __init__(self, requester) -> None:
       self.requester = requester 
