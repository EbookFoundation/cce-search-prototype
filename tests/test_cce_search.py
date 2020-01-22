# Main test file
# Reference: https://flask.palletsprojects.com/en/1.1.x/testing/

import os
import sys
import tempfile

import pytest

# Try to configure top level directory to fix import error --> doesn't fix it yet
# project_dir = os.path.join(os.path.dirname(__file__), "..")
# sys.path.append(project_dir)

# This is incorrect, cce_search is not currently importable
from cce_search import cce_search

# Create the client fixture used by tests
@pytest.fixture
def client():
    # In __init__.py, 'DATABASE' is commented out --> issue?
    db_fd, cce_search.app.config['DATABASE'] = tempfile.mkstemp()
    cce_search.app.config['TESTING'] = True
    
    with cce_search.app.test_client() as client:
        with cce_search.app.app_context():
            cce_search.init_db()
        yield client
        
    os.close(db_fd)
    os.unlink(cce_search.app.config['DATABASE'])
    

# TODO: Possible functions/features to test:
#       - Constructing app without errors (overall integration test)
#       - Search results (feature test)