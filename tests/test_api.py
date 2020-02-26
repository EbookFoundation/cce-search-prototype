""" 
Note:
Some of the values in the returned objects are lists (including many 1 element lists), e.g.:
    {
        "results": [
            {
                "authors": [
                    ...
                ],
                "pages": ...,
                
            }
        ]
    }
This is why many lines contain a mix of keys and indices, such as ["key_1"][1]["key_2"][0]["key_3"]
"""

import pytest
import requests

API = "http://sfr-bardo-copyright-development.us-east-1.elasticbeanstalk.com"
REG_UUID = "b055bda4-6f10-1014-90c3-93bd933bf4a5"
RENEW_UUID = "cce7b1b5-c98e-59cf-8063-f020da28cdd3"
REG_NUM = "A71297"
RENEW_NUM = "R673507"

# Test that the API can be reached successfully
def test_basic_api_connection(client):
    res = requests.get(API)
    assert res.status_code == 200

# Test the registration number lookup service
def test_registration_lookup(client):
    res = requests.get(API + "/registration/" + REG_UUID)
    json_res = res.json()
    assert json_res["data"]["authors"] == ["Cary F. Baynes", "C. G. Jung", "Hellmut Wilhelm"]

# Test the renewal number lookup service
def test_renewal_lookup(client):
    res = requests.get(API + "/renewal/" + RENEW_UUID)
    json_res = res.json()
    assert json_res["data"][0]["registrations"][0]["date"] == "1950-05-25"

# Test the fulltext search service is working
def test_fulltext_search(client):
    res = requests.get(API + "/search/fulltext?query=I%20Ching")
    json_res = res.json()
    assert len(json_res["data"]["results"]) == 10 # TODO: Improve this

# Test the registration number search service is working
def test_registration_search(client):
    res = requests.get(API + "/search/registration/" + REG_NUM)
    json_res = res.json()
    assert json_res["data"]["results"][1]["registrations"][0]["number"] == REG_NUM

# Test the renewal number search service is working
def test_renewal_search(client):
    res = requests.get(API + "/search/renewal/" + RENEW_NUM)
    json_res = res.json()
    assert json_res["data"]["results"][0]["renewals"][0]["renewal_num"] == RENEW_NUM
