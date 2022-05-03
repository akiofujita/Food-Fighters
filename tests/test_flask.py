""" Tests flask functionality """
import sys
import json
sys.path.append('.')
import backend.project as project
import mysql.connector

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
  Tests form submission and search by ensuring that the recently added submission exists
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
    
  """
  # Check database 
  cnx = mysql.connector.connect(user='root', password='ffDB2022!', host = '34.72.233.63', database='FoodFighters')
  cursor = cnx.cursor(buffered=True)
  cursor.execute("SELECT COUNT(RecipeID) FROM recipe WHERE name = 'Test'")
  count = cursor.fetchone()[0]
  cnx.commit()
  cursor.close()
  assert (count > 0) 
  """
      
      
def test_search():
  """
  Moving onto searching for it
  """
  with flask_app.test_client() as test_client:
    # Sample recipe to add
    response = test_client.get('/searchrecipe', data={
        "searchStr": "test",
    })
    # If these are true, then we've successfully submitted
    a = json.loads(response)
    assert a['num_recipes'] >= 1
  
  """
  # Delete from database when done to ensure that this is checked every time
  cnx = mysql.connector.connect(user='root', password='ffDB2022!', host = '34.72.233.63', database='FoodFighters')
  cursor = cnx.cursor(buffered=True)
  cursor.execute("SELECT RecipeID FROM foodfighters.recipe WHERE name = Test")
  RecipeID = cursor.fetchone()[0]
  cursor.execute("DELETE FROM ingredient WHERE name = 'test'; DELETE FROM recipe WHERE total_time = 9999999; DELETE FROM quantity WHERE QRecipeID = %s; DELETE FROM steps WHERE direction = 'Ignore this :)'", [RecipeID])
  cnx.commit()
  cursor.close()
  """
      
      
      

