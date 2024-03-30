from unittest import mock

from .requests_client import Collection


#
# LIST
#
def test_list_params_is_valid():
    mock_requester = mock.Mock()
    m_employee = Collection(mock_requester, {"name": "test"})
    m_employee.list()
    mock_requester.list.return_value = {"data": []}
    mock_requester.list.assert_called_with(
        "test",
        {"sort": [], "fields": [], "appends": [], "except": []}
    )

#
# GET
#
def test_get_params_is_valid():
    mock_requester = mock.Mock()
    m_employee = Collection(mock_requester, {"name": "test"})
    m_employee.get(id=1)
    mock_requester.get.assert_called_with(
        "test",
        {"filterByTk": 1, "sort": [], "fields": [], "appends": [], "except": []}
    )

def test_get_with_filter_is_valid():
    mock_requester = mock.Mock()
    m_employee = Collection(mock_requester, {"name": "test"})
    m_employee.get(filter={"emp_id": 1})
    mock_requester.get.assert_called_with(
        "test",
        {"filter": '{"emp_id": 1}',"sort": [], "fields": [], "appends": [], "except": []}
    )

#
# Create
#
def test_create_params_is_valid():
    mock_requester = mock.Mock()
    m_employee = Collection(mock_requester, {"name": "test"})
    m_employee.create(body={"key": "value"})
    mock_requester.create.assert_called_with(
        "test", {"whitelist": [], "blacklist": []}, {"key": "value"}
    )


def test_create_with_whitelist_is_valid():
    mock_requester = mock.Mock()
    m_employee = Collection(mock_requester, {"name": "test"})
    whitelist = ["field1"]
    blacklist = ["field2"]
    m_employee.create(whitelist=whitelist, blacklist=blacklist, body={"key": "value"})
    mock_requester.create.assert_called_with(
        "test", {"whitelist": ["field1"], "blacklist": ["field2"]}, {"key": "value"}
    )


#
# Update
#
def test_update_params_is_valid():
    mock_requester = mock.Mock()
    m_employee = Collection(mock_requester, {"name": "test"})
    m_employee.update(id=1, body={"key": "new value"})
    mock_requester.update.assert_called_with(
        "test",
        {"filterByTk": 1, "whitelist": [], "blacklist": []},
        {"key": "new value"},
    )


def test_update_with_filter_is_valid():
    mock_requester = mock.Mock()
    m_employee = Collection(mock_requester, {"name": "test"})
    m_employee.update(filter={"emp_id": 1}, body={"key": "new value"})
    mock_requester.update.assert_called_with(
        "test",
        {"filter": '{"emp_id": 1}', "whitelist": [], "blacklist": []},
        {"key": "new value"},
    )


def test_update_with_whitelist_is_valid():
    mock_requester = mock.Mock()
    m_employee = Collection(mock_requester, {"name": "test"})
    whitelist = ["field1"]
    blacklist = ["field2"]
    m_employee.update(
        filter={"emp_id": 1},
        whitelist=whitelist,
        blacklist=blacklist,
        body={"key": "new value"},
    )
    mock_requester.update.assert_called_with(
        "test",
        {"filter": '{"emp_id": 1}', "whitelist": ["field1"], "blacklist": ["field2"]},
        {"key": "new value"},
    )
