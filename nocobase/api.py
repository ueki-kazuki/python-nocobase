from typing import Optional
from urllib.parse import urljoin
from enum import Enum


class NocobaseAPIUris(Enum):
    V1_DB_DATA_PREFIX = "api/"
    V1_DB_META_PREFIX = "api/"


class NocobaseAPI:
    def __init__(self, base_uri: str):
        self.__base_data_uri = urljoin(
            base_uri + "/", NocobaseAPIUris.V1_DB_DATA_PREFIX.value
        )
        # self.__base_meta_uri = urljoin(base_uri + "/", NocobaseAPIUris.V1_DB_META_PREFIX.value)

    def get_collections_uri(self) -> str:
        return (
            urljoin(
                self.__base_data_uri,
                "/".join(("collections",)),
            )
            + ":list"
        )

    def get_collection_uri_for(self, collection: str, operation: Optional[str] = "list") -> str:
        return "{}:{}".format(
            urljoin(
                self.__base_data_uri,
                "/".join((collection,)),
            ),
            operation
        )
