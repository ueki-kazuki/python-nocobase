from abc import ABC, abstractmethod

class AuthToken(ABC):
    @abstractmethod
    def get_header(self) -> dict:
        pass


class JWTAuthToken(AuthToken):
    def __init__(self, token: str):
        self.__token = token

    def get_header(self) -> dict:
        return {"Authorization": f"Bearer {self.__token}"}
