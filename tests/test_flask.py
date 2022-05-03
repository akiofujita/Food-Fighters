""" Tests flask functionality """
import sys
sys.path.append('.')
import backend.project as project

flask_app = project.create_app('flask_test.cfg')

def test_homepage():
  """
  Tests homepage by asserting a status code of 200 to ensure appliation is reachable and running
  """
  with flask_app.test_client() as test_client:
    response = test_client.get('/')
    print(response.status_code == 200)
    assert response.status_code == 200
