""" This is the app.py module that keeps tracks of the various webapp routes """
import sqlite3
import flask
from flask_restx import Resource, Api

app = flask.Flask(__name__)
api = Api(app)

unitsMap = {
  'met-0': 'grams',
  'imp-0': 'tbsp',
  'misc-0': 'pinch'
}

def convertUnits(idList):
  return [unitsMap[id] for id in idList]
  
def parseIngredients(ingString):
  return ingString.split(', ')

def orgRecipe(recipeList):
  for i in range(len(recipeList)):
    newIng = parseIngredients(recipeList[i][1])
    newRecipe = (recipeList[i][0], newIng, recipeList[i][2])
    recipeList[i] = newRecipe
  return recipeList

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
    try:
      conn = sqlite3.connect('data/recipes.db')
      cursor = conn.cursor()

      form = flask.request.form
      recipe_title = form.getlist('recipe_title')[0]
      recipe_desc = form.getlist('recipe_desc')[0]
      total_time = form.getlist('total_time')[0]
      ing_names = form.getlist('ing_name')
      ing_quants = form.getlist('ing_quant')
      ing_units = convertUnits(form.getlist('ing_units'))
      steps = form.getlist('steps')

      if (len(ing_names) != len(ing_quants) or len(ing_names) != len(ing_units) or len(ing_quants) != len(ing_units)):
        raise LengthError
      
      ingredients = []
      for i in range(len(ing_names)):
        ingredients.append((ing_names[i], ing_quants[i], ing_units[i]))

      print('Recipe Title: ' + recipe_title)
      print('Recipe Desc : ' + recipe_desc)
      print('Total Time  : ' + total_time)
      print('Ingredients : ')
      print(ingredients)
      print('Steps       : ')
      print(steps)

      conn.commit()
      conn.close()

      return flask.redirect("http://localhost:3000/Add")
    
    except LengthError:
      print("Ingredient List Length Error")
      return flask.redirect("http://localhost:3000")

    except Exception as e:
      print(e)
      return flask.redirect("http://localhost:3000")

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
    recipes = orgRecipe(recipes)

    print(recipes)
    print(numRecipes)
    
    conn.close()
    return {
      'num_recipes': numRecipes,
      'recipes': recipes
    }

def main():
  app.run()

if __name__ == '__main__':
  main()