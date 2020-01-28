import pytest

# TODO: Possible functions/features to test:
#       - Search results (feature test)


# Test that the application successfully serves the main page
def test_search_page(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b'Unofficial copyright search prototype' in res.data

# Test that a successful search yields results
def test_search_functioning(client):
    # Search for a title that we know will result in numerous matches
    res = client.get("/?type=ft&term=I+Ching")
    assert res.status_code == 200
    

