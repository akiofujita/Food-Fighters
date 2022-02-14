import pytest
import sys
import json
sys.path.append('.')

import backend.app as app

def test_homepage():
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert "<h1>Homepage</h1>" in response.data