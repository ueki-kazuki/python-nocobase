from .nocobase import AuthToken, JWTAuthToken


def test_authtoken():
    token = "abcd1234"
    auth: AuthToken = JWTAuthToken(token)
    expect = {"Authorization": "Bearer abcd1234"}
    assert expect == auth.get_header()
