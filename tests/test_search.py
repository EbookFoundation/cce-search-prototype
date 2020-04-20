import pytest

# Test that the application successfully serves the main page
def test_search_page(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b'<form>' in res.data

# Test that a successful title search yields results
def test_successful_title_search(client):
    res = client.get("/?title=Jungle&author=&publisher=&registration=&renewal=")
    assert res.status_code == 200
    assert b'<div class = "results">' in res.data

# Test that an unsuccessful title search renders an error message
def test_unsuccessful_title_search(client):
    res = client.get("/?title=blahhblahblahblah&author=&publisher=&registration=&renewal=")
    assert res.status_code == 200
    assert b'No results found. Please try another search.' in res.data

# Test that a successful author search yields results
def test_successful_author_search(client):
    res = client.get("/?title=&author=Smith&publisher=&registration=&renewal=")
    assert res.status_code == 200
    assert b'<div class = "results">' in res.data

# Test that an unsuccessful title search renders an error message
def test_unsuccessful_author_search(client):
    res = client.get("/?title=&author=IAMNOTANAUTHOR&publisher=&registration=&renewal=")
    assert res.status_code == 200
    assert b'No results found. Please try another search.' in res.data

# Test that a successful publisher search yields results
def test_successful_publisher_search(client):
    res = client.get("/?title=&author=&publisher=Penguin&registration=&renewal=")
    assert res.status_code == 200
    assert b'<div class = "results">' in res.data

# Test that an unsuccessful publisher search renders an error message
def test_unsuccessful_publisher_search(client):
    res = client.get("/?title=&author=&publisher=FAKEPUBLISHERINC&registration=&renewal=")
    assert res.status_code == 200
    assert b'No results found. Please try another search.' in res.data

# Test that a successful registration number search yields results
def test_successful_registration_number_search(client):
    res = client.get("/?title=&author=&publisher=&registration=A45173&renewal=")
    assert res.status_code == 200
    assert b'<div class = "results">' in res.data

# Test that an unsuccessful registration number search renders an error message
def test_unsuccessful_registration_number_search(client):
    res = client.get("/?title=&author=&publisher=&registration=NOTANUMBER&renewal=")
    assert res.status_code == 200
    assert b'No results found. Please try another search.' in res.data
    
# Test that a successful renewal number search yields results
def test_successful_renewal_number_search(client):
    res = client.get("/?title=&author=&publisher=&registration=&renewal=R673507")
    assert res.status_code == 200
    assert b'<div class = "results">' in res.data

# Test that an unsuccessful registration number search renders an error message
def test_unsuccessful_renewal_number_search(client):
    res = client.get("/?title=&author=&publisher=&registration=&renewal=NOTANUMBER")
    assert res.status_code == 200
    assert b'No results found. Please try another search.' in res.data