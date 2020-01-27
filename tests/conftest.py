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
    # Create temp file to hold db for testing
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({'TESTING': True, 'DATABASE': db_path}) # In __init__.py, 'DATABASE' is commented out --> issue?

    # TODO: Create database --> our project differs here

    yield app
        
    os.close(db_fd)
    os.unlink(db_path)

# Create the test client
@pytest.fixture
def client(app):
    return app.test_client()