import pytest

from bs4 import BeautifulSoup

# Test that the application successfully serves the main page
def test_search_page(client):
    res = client.get("/")
    assert res.status_code == 200
    page = BeautifulSoup(res.data, 'html.parser')
    assert page.title.string == "Find Copyright Entries - CCE Search"

# Test that a successful search yields results
def test_search_functioning(client):
    # Search for a title that we know will result in numerous matches
    res = client.get("/?type=ft&term=I+Ching")
    assert res.status_code == 200
    page = BeautifulSoup(res.data, 'html.parser')
    # print(page.prettify())
    # print(page.title)
    assert res.status_code == 200