""" Tests flask functionality """
import sys
sys.path.append('.')
from backend.project import create_app

flask_app = create_app('flask_test.cfg')

def test_homepage():
  """
  Tests homepage by asserting a status code of 200 to ensure appliation is reachable and running
  """
  with flask_app.test_client() as test_client:
    response = test_client.get('/')
    assert response.status_code == 200
