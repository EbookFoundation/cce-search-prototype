import pytest

from bs4 import BeautifulSoup

# TODO: Update these tests to comply with the updated UI

# Test that the application successfully serves the main page
def test_search_page(client):
    res = client.get("/")
    assert res.status_code == 200
    page = BeautifulSoup(res.data, 'html.parser')
    assert page.title.string == "Copyright Renewals"

# Test that a successful title search yields results
def test_successful_title_search(client):
    res = client.get("/?title=Jungle&author=&publisher=&registration=&renewal=")
    assert res.status_code == 200
    assert b'<div class = "results">' in res.data

# Test that an unsuccessful full text search returns to the home screen
# def test_unsuccessful_full_text_search(client):
    # res = client.get("/?type=ft&term=blahblahblahblahblahblah")
    # assert res.status_code == 200
    # result_page = BeautifulSoup(res.data, 'html.parser')
    # home_res = client.get("/")
    # home_page = BeautifulSoup(home_res.data, 'html.parser')
    # assert result_page.string == home_page.string

# Test that a successful registration number search yields results
def test_successful_registration_number_search(client):
    res = client.get("/?title=&author=&publisher=&registration=A45173&renewal=")
    assert res.status_code == 200
    assert b'<div class = "results">' in res.data

# Test that an unsuccessful registration number search returns to the home screen
# def test_unsuccessful_registration_number_search(client):
#     res = client.get("/?type=reg&term=ThisIsNotARegistrationNumber")
#     assert res.status_code == 200
#     result_page = BeautifulSoup(res.data, 'html.parser')
#     home_res = client.get("/")
#     home_page = BeautifulSoup(home_res.data, 'html.parser')
#     assert result_page.string == home_page.string
    
# Test that a successful renewal number search yields results
def test_successful_renewal_number_search(client):
    res = client.get("/?title=&author=&publisher=&registration=&renewal=R673507")
    assert res.status_code == 200
    assert b'<div class = "results">' in res.data

# Test that an unsuccessful registration number search returns to the home screen
# def test_unsuccessful_renewal_number_search(client):
#     res = client.get("/?type=ren&term=ThisIsNotARenewalNumber")
#     assert res.status_code == 200
#     result_page = BeautifulSoup(res.data, 'html.parser')
#     home_res = client.get("/")
#     home_page = BeautifulSoup(home_res.data, 'html.parser')
#     assert result_page.string == home_page.string