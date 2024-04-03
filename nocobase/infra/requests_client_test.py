from unittest import mock

import pytest
import requests

from .requests_client import (
    Collection,
    NocoBaseRequestsClient,
    requests as requests_lib,
)
from ..exceptions import NocoBaseAPIError, NocoBaseCollectionNotFoundError


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


@mock.patch.object(requests_lib, "Session")
def test_session_request_correctory_called_from_list_collections(mock_requests_session):
    mock_session = mock.Mock()
    mock_requests_session.return_value = mock_session

    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"data": []}
    mock_session.request.return_value = mock_resp

    client = NocoBaseRequestsClient(mock.Mock(), "")
    client.list_collections()
    mock_session.request.assert_called_once_with("GET", "/api/collections:list")


@mock.patch.object(requests_lib, "Session")
def test_session_request_correctory_called_from_list(mock_requests_session):
    mock_session = mock.Mock()
    mock_requests_session.return_value = mock_session

    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "data": [{"id": 1, "name": "sample"}],
        "meta": {"page": 1, "pageSize": 20, "totalPage": 1},
    }
    mock_session.request.return_value = mock_resp

    client = NocoBaseRequestsClient(mock.Mock(), "")
    _ = list(client.list(collection="sample", params={}))
    mock_session.request.assert_called_once_with("GET", "/api/sample:list", params={})


@mock.patch.object(requests_lib, "Session")
def test_request_correctory_called_from_list_collections(mock_requests_session):
    mock_requests_session.return_value = mock.Mock()
    mock_request = mock.Mock()
    client = NocoBaseRequestsClient(mock.Mock(), "")
    with mock.patch.object(client, "_request") as mock_request:
        mock_resp = mock.Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"data": []}
        mock_request.return_value = mock_resp

        client.list_collections()
        mock_request.assert_called_once_with("GET", "/api/collections:list")


@mock.patch.object(requests_lib, "Session")
def test_collection(mock_requests_session):
    mock_session = mock.Mock()
    mock_requests_session.return_value = mock_session

    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"data": [{"name": "sample"}]}
    mock_session.request.return_value = mock_resp

    client = NocoBaseRequestsClient(mock.Mock(), "")
    collection = client.collection("sample")
    assert type(collection) is Collection
    mock_session.request.assert_called_once_with("GET", "/api/collections:list")


@mock.patch.object(requests_lib, "Session")
def test_collection_notfound(mock_requests_session):
    mock_session = mock.Mock()
    mock_requests_session.return_value = mock_session

    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"data": [{"name": "sample"}]}
    mock_session.request.return_value = mock_resp

    client = NocoBaseRequestsClient(mock.Mock(), "")
    with pytest.raises(NocoBaseCollectionNotFoundError) as exc_info:
        _ = client.collection("not_exist")
    mock_session.request.assert_called_once_with("GET", "/api/collections:list")
    assert exc_info.value.args[0] == "Collection not_exist is not found"
