import pytest
import sys
import json
sys.path.append('.')

import backend.project as project

flask_app = project.create_app('flask_test.cfg')

def test_homepage():
     with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
