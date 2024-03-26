from unittest import mock

import pytest
import requests

from .requests_client import NocoBaseRequestsClient, requests as requests_lib
from ..exceptions import NocoBaseAPIError


@mock.patch.object(requests_lib, "Session")
def test_NocoBaseAPIError_raised_on_bad_response(mock_requests_session):
    mock_session = mock.Mock()
    mock_resp = requests.models.Response()
    mock_resp.status_code = 401
    mock_requests_session.return_value = mock_session
    mock_session.request.return_value = mock_resp

    client = NocoBaseRequestsClient(mock.Mock(), "")
    with pytest.raises(NocoBaseAPIError) as exc_info:
        client._request("GET", "/")

    assert exc_info.value.status_code == 401
