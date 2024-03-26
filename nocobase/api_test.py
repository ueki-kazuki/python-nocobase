import pytest

from .api import NocoBaseAPI, NocoBaseAPIUris


def test_get_collections_uri():
    localhost = "http://localhost:13000"
    api = NocoBaseAPI(localhost)
    expect = "{}/{}{}:{}".format(
        localhost,
        NocoBaseAPIUris.V1_DB_DATA_PREFIX.value,
        "collections",
        "list",
    )
    assert expect == api.get_collections_uri()


def test_get_collection_uri():
    localhost = "http://localhost:13000"
    api = NocoBaseAPI(localhost)
    expect = "{}/{}{}:{}".format(
        localhost,
        NocoBaseAPIUris.V1_DB_DATA_PREFIX.value,
        "sample",
        "list",
    )
    assert expect == api.get_collection_uri_for("sample")


def test_get_collection_uri_with_operation():
    localhost = "http://localhost:13000"
    api = NocoBaseAPI(localhost)
    expect = "{}/{}{}:{}".format(
        localhost,
        NocoBaseAPIUris.V1_DB_DATA_PREFIX.value,
        "sample",
        "get",
    )
    assert expect == api.get_collection_uri_for("sample", "get")
