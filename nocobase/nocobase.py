from abc import ABC, abstractmethod
from typing import Optional, List


class AuthToken(ABC):
    @abstractmethod
    def get_header(self) -> dict:
        pass


class JWTAuthToken(AuthToken):
    def __init__(self, token: str):
        self.__token = token

    def get_header(self) -> dict:
        return {"Authorization": f"Bearer {self.__token}"}


class NocoBaseClient:
    @abstractmethod
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
        pass

    @abstractmethod
    def get(
        self,
        id: Optional[int] = None,
        filter: Optional[dict] = None,
        sort: List[str] = [],
        fields: List[str] = [],
        appends: List[str] = [],
        excepts: List[str] = [],
    ) -> dict:
        pass

    @abstractmethod
    def create(
        self,
        body: dict,
        whitelist: List[str] = [],
        blacklist: List[str] = [],
    ) -> dict:
        pass

    @abstractmethod
    def update(
        self,
        body: dict,
        id: Optional[int] = None,
        filter: Optional[dict] = None,
        whitelist: List[str] = [],
        blacklist: List[str] = [],
    ) -> dict:
        pass

    @abstractmethod
    def destroy(
        self,
        id: Optional[int] = None,
        filter: Optional[dict] = None,
    ) -> dict:
        pass
