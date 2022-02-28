""" This is the app.py module that keeps tracks of the various webapp routes """
import sqlite3
import flask

api = flask.Flask(__name__)

@api.route("/")
def landing():
  """ Landing API, probably deprecated/uncessary """
  return "<h1>Homepage</h1>"

@api.route("/addrecipe")
def addrecipe():
  """ Explanation goes here. """
  return flask.render_template("/recipes.html")

@api.route("/submitrecipe", methods = ['POST'])
def submitrecipe():
  """ Explanation goes here. """
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

  return flask.redirect("http://localhost:3000/Recipe")

@api.route("/display", methods = ['GET'])
def display():
  """ 
  Test display function. Grabs all recipes from database
  and send to React for display on UI.
  """
  conn = sqlite3.connect('data/recipes.db')
  cursor = conn.cursor()
  
  columns = 'recipe_id, recipe_name, prep_time'
  cursor.execute(f'''SELECT {columns} FROM recipes;''')

  data = cursor.fetchall()
  recipes = sort_by_time(data)

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
