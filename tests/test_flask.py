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
    assert response.status_code == 200
    

def test_submit():
  """
  Tests form submission by asserting a status code of 320, meaning that it's been redirected to the /add page
  """
  with flask_app.test_client() as test_client:
    # Sample recipe to add
    response = test_client.post('/submitrecipe', data={
      "recipe_title": "Test",
      "recipe_desc": "Test description",
      "total_time": "9999999",
      "serving_size": "1",
      "ing_name": "test",
      "ing_quant": "1",
      "ing_units": "",
      "steps": "Ignore this :)",
  })
    # If these are true, then we've successfully redirected and submitted
    assert response.status_code == 302


def test_search():
  with flask_app.test_client() as test_client:
    # Sample recipe to add
    response = test_client.get('/searchrecipe', data={
        "searchStr": "onion",
    })
    # If these are true, then we've successfully submitted
    print(response.data)
    assert response.data['num_recipes'] >= 1
