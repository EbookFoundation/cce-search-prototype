import pytest

# TODO: Possible functions/features to test:
#       - Search results (feature test)

# Test that the application can build and serve the home page
# This is a very hacked together way to test this, may try to improve it at some point but for now it works
def test_app_runs(client):
    res = client.get("/")
    assert b'Unofficial copyright search prototype' in res.data