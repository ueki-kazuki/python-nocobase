from typing import Optional


class NocoBaseAPIError(Exception):
    def __init__(
        self,
        message: str,
        status_code: int,
        response_json: Optional[dict] = None,
        response_text: Optional[str] = None,
    ):
        super().__init__(message)
        self.status_code = status_code
        self.response_json = response_json
        self.response_text = response_text


class NocoBaseCollectionNotFoundError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
