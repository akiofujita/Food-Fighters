import sqlite3
import flask


api = flask.Flask(__name__)


"""
high level support for doing this and that.
"""
@api.route("/")
def hello_world():
    return "<h1>Homepage</h1>"

"""
high level support for doing this and that.
"""
@api.route("/addrecipe")
def addrecipe():
    return flask.render_template("/recipes.html")

"""
high level support for doing this and that.
"""
@api.route("/submitrecipe", methods = ['POST'])
def submitrecipe():
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
