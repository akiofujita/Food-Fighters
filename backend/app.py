""" This is the app.py module that keeps tracks of the various webapp routes """
import email
import sqlite3
import flask
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

app = flask.Flask(__name__)
api = Api(app)

IP = '34.70.168.238'
user = 'root'
passwd = 'ffDB2022!'
db = 'FoodFighters'
# project_id = 'nth-gasket-348415'
instance_name = 'nth-gasket-348415:us-central1:food-fighters-db'
# URI = r'mysql+pymysql://'+user+r':'+passwd+r'@'+IP+r'/'+db
URI = f'mysql+mysqldb://{user}:{passwd}@{IP}/{db}?unix_socket=/cloudsql/{instance_name}'
print(URI)

# Configuration
app.config['SECRET_KEY'] = 'ffDB2022!'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

@api.route("/")
@api.deprecated
class Index(Resource):
  def get(self):
    """ Index API, probably deprecated/uncessary """
    return "<h1>Homepage</h1>"

@api.route("/addrecipe", endpoint="addrecipe")
@api.deprecated
class addRecipe(Resource):
  def get(self):
    """ Deprecated. """
    return flask.render_template("/recipes.html")

@api.route("/submitrecipe", endpoint="submitrecipe")
class submitRecipe(Resource):
  def post(self):
    """ API for submitting a recipe to the database. """
    conn = sqlite3.connect('data/recipes.db')
    cursor = conn.cursor()

    recipe_name = flask.request.form['recipe_name']
    ingredients = flask.request.form['ingredients']
    time = flask.request.form['prep_time']
    steps = flask.request.form['steps']

    cursor.execute(f'''INSERT INTO recipes (recipe_name, ingredients, prep_time, steps, poster_id) \
                    VALUES("{recipe_name}", "{ingredients}", {time}, "{steps}", {-1})''')
    conn.commit()
    conn.close()

    return flask.redirect("http://localhost:3000/Add")

@api.route("/display", endpoint="display")
@api.deprecated
class display(Resource):
  def get(self):
    """
    Test display function. Grabs all recipes from database
    and send to React for display on UI.
    """
    conn = sqlite3.connect('data/recipes.db')
    cursor = conn.cursor()

    columns = 'recipe_id, recipe_name, prep_time'
    cursor.execute(f'''SELECT {columns} FROM recipes;''')

    data = cursor.fetchall()
    recipes = self.sort_by_time(data)

    # Choose recipe with longest prep time
    # name = recipes[-1][1]

    # Choose recipe with shortest prep time
    name = recipes[0][1]

    conn.close()
    return {'recipe_name': name}

  def sort_by_time(recipes):
    """
    Sorts a list of elements formatted as (recipe_id, recipe_name, prep_time)
    by prep_time.
    """
    sorted_recipes = sorted(recipes, key = lambda x: x[2]) # Sorts by third element of tuple
    return sorted_recipes

@api.route("/getcard", endpoint="getcard")
class getcard(Resource):
  def get(self):
    """ 
    Test display function. Grabs all recipes from database
    and send to React for display on UI.
    """
    conn = sqlite3.connect('data/recipes.db')
    cursor = conn.cursor()
    
    columns = 'recipe_name, ingredients, prep_time'
    cursor.execute(f'''SELECT {columns} FROM recipes;''')

    recipes = cursor.fetchall()

    name = recipes[-1][0]
    ings = recipes[-1][1]
    time = recipes[-1][2]
    
    conn.close()
    return {
      'recipe_name': name,
      'ingredients': ings,
      'prep_time': time
    }

@api.route("/displaycards", endpoint="displaycards")
class displaycards(Resource):
  def get(self):
    """ 
    Test display function. Grabs all recipes from database
    and send to React for display on UI.
    """
    conn = sqlite3.connect('data/recipes.db')
    cursor = conn.cursor()
    
    columns = 'recipe_name, ingredients, prep_time'
    cursor.execute(f'''SELECT {columns} FROM recipes;''')

    recipes = cursor.fetchall()
    numRecipes = len(recipes)
    # print(recipes)
    # print(numRecipes)
    
    conn.close()
    return {
      'num_recipes': numRecipes,
      'recipes': recipes
    }

class Recipe(db.Model):
  RecipeID = db.Column(INTEGER, unique=True, primary_key=True)
  name = db.Column(VARCHAR(45), unique=True, nullable=False)
  description = db.Column(MEDIUMTEXT)
  prepTime = db.Column(INTEGER, nullable=False)
  cookTime = db.Column(INTEGER, nullable=False)
  author = db.Column(INTEGER, db.ForeignKey('user.UserID'), nullable=False)
  servingSize = db.Column(INTEGER, nullable=False)

class User(db.Model):
  UserID = db.Column(INTEGER, unique=True, primary_key=True)
  username = db.Column(VARCHAR(16), unique=True, nullable=False)
  email = db.Column(VARCHAR(255), unique=True, nullable=False)
  password = db.Column(VARCHAR(32), nullable=False)
  create_time = db.Column(TIMESTAMP, nullable=False)
  recipes = db.relationship('Recipe', backref='recipe_author', lazy=True)

def main():
  test_recipe = Recipe.query.filter_by(name='Beef Noodle Soup').first()
  print('test\n')
  print(test_recipe.id)
  # app.run()

if __name__ == '__main__':
  main()
