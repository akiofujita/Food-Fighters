""" Conftest.py helps configure the flask app """
import sys
import pytest
sys.append('.')
import backend.project as project

@pytest.fixture()
def test_client():
  """
  Pytest fixture that sets up a dummy client under the flask_test configurations. 
  Establishes a connection with the application for testing Flask functionality.
  """
  flask_app = project.create_app('flask_test.cfg')

  # Create a test client using the Flask application configured for testing
  with flask_app.test_client() as testing_client:
    # Establish an application context
    with flask_app.app_context():
      yield testing_client  # this is where the testing happens!
