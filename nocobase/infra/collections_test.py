from unittest import mock

from .requests_client import Collections


#
# Collections LIST
#
def test_list_params_is_valid():
    mock_requester = mock.Mock()
    mock_requester.list_collections.return_value = []
    collections = Collections(mock_requester)
    collections.list()
    mock_requester.list_collections.assert_called_once()


#
# Collections GET
#
def test_get_params_is_valid():
    mock_requester = mock.Mock()
    mock_requester.list_collections.return_value = []
    collections = Collections(mock_requester)
    collections.get("sample")
    mock_requester.list_collections.assert_called_once()
