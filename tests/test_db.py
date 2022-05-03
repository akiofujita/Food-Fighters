""" Checks if CI can connect and properly query from database """
import mysql.connector
def test_db():
  """
  Using cursor, connect to database service and query a count of recipes.
  If counts are > 0, then db is populated and should query properly.
  Only recipes are taken into account becase if recipes don't exist it cascades
  """
  cnx = mysql.connector.connect(user='root', password='ffDB2022!', host = '34.72.233.63', database='FoodFighters')

  cursor = cnx.cursor(buffered=True)
  
  cursor.execute("SELECT COUNT(RecipeID) FROM recipe WHERE RecipeID >= 1")
  count = cursor.fetchone()[0]
  cnx.commit()
  cursor.close()
  assert (count > 0)
