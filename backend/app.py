""" This is the app.py module that keeps tracks of the various webapp routes """
import sqlite3
import flask

api = flask.Flask(__name__)

@api.route("/")
def hello_world():
  """ Explanation goes here. """
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
  steps = flask.request.form['steps']

  cursor.execute(f'''INSERT INTO recipes (recipe_name, ingredients, steps, poster_id) \
                  VALUES("{recipe_name}", "{ingredients}", "{steps}", {-1})''')
  conn.commit()
  conn.close()

  return flask.redirect("/")
