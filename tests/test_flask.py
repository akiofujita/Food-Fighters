import pytest
import sys
import json
sys.path.append('.')

import backend.app as app

def test_homepage():
    response = app.get('/')
    assert response.status_code == 200
    assert "<h1>Homepage</h1>" in response.data