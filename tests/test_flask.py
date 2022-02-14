import pytest
import sys
import json
from backend.project import create_app

flask_app = create_app('flask_test.cfg')

def test_homepage():
     with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
