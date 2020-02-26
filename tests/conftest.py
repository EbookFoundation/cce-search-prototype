# Reference: https://flask.palletsprojects.com/en/1.1.x/testing/ 
# THIS MAY BE OUT OF DATE, SEE: https://github.com/pallets/flask/blob/master/examples/tutorial/tests/conftest.py

# Note: currently, you must run tests with python -m pytest from the main project directory

import os
import tempfile

import pytest

from cce_search import create_app

# Create the client fixture used by tests
@pytest.fixture
def app():
    app = create_app({'TESTING': True})

    yield app

# Create the test client
@pytest.fixture
def client(app):
    return app.test_client()