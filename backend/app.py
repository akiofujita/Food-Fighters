""" This is the app.py module that keeps tracks of the various webapp routes """
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
api = Api(app, version='1.0.0', title='Food Fighters API', description='A set of APIs for the open source Food Fighters project')

IP = '34.72.233.63'
user = 'root'
passwd = 'ffDB2022!'
db = 'FoodFighters'
instance_name = 'nth-gasket-348415:us-central1:food-fighters'
URI = f'mysql+mysqldb://{user}:{passwd}@{IP}/{db}?unix_socket=/cloudsql/{instance_name}'

# Configuration
app.config['SECRET_KEY'] = 'ffDB2022!'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# SQLAlchemy models
class Recipe(db.Model):
  RecipeID = db.Column(INTEGER, unique=True, primary_key=True)
  name = db.Column(VARCHAR(45), unique=True, nullable=False)
  description = db.Column(MEDIUMTEXT)
  totalTime = db.Column(INTEGER, nullable=False)
  author = db.Column(INTEGER, db.ForeignKey('user.UserID'), nullable=False)
  servingSize = db.Column(INTEGER, nullable=False)
  quantities = db.relationship('Quantity', backref='quantity_RecipeID', lazy='joined')

class User(db.Model):
  UserID = db.Column(INTEGER, unique=True, primary_key=True)
  username = db.Column(VARCHAR(16), unique=True, nullable=False)
  email = db.Column(VARCHAR(255), unique=True, nullable=False)
  password = db.Column(VARCHAR(32), nullable=False)
  create_time = db.Column(TIMESTAMP, nullable=False)
  recipes = db.relationship('Recipe', backref='recipe_author', lazy=True)

class Quantity(db.Model):
  QRecipeID = db.Column(INTEGER, db.ForeignKey('recipe.RecipeID'), primary_key=True)
  QIngredientID = db.Column(INTEGER, db.ForeignKey('ingredient.IngredientID'), primary_key=True)
  value = db.Column(FLOAT, nullable=False)
  measurement = db.Column(VARCHAR(45), nullable=False)
  state = db.Column(VARCHAR(45))

class Ingredient(db.Model):
  IngredientID = db.Column(INTEGER, unique=True, primary_key=True)
  name = db.Column(VARCHAR(45), nullable=False)
  quantities = db.relationship('Quantity', backref='quantity_IngredientID', lazy=True)

class Steps(db.Model):
  StepsRecipeID = db.Column(INTEGER, db.ForeignKey('recipe.RecipeID'), primary_key=True)
  order = db.Column(INTEGER, unique=True, primary_key=True)
  direction = db.Column(MEDIUMTEXT, nullable=False)

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

def formatRecipes(recipes):
  recipesList = []
  for recipe in recipes:
    recipe_name = recipe.name
    rID = recipe.RecipeID
    time = recipe.totalTime
    # obtain ingredients
    quants = Quantity.query.filter_by(QRecipeID=rID).all()
    ingredients = ''
    for quant in quants:
      ingID = quant.QIngredientID
      ing = Ingredient.query.filter_by(IngredientID=ingID).first()
      amount = quant.value
      unit = quant.measurement
      ing_name = ing.name
      ingredients += f'{amount} {unit} {ing_name}, '
    ingredients = ingredients[:-2]
    recipesList.append([recipe_name, ingredients, time])
  # Sort by time
  recipesList.sort(key = lambda x: x[2])
  recipes = orgRecipe(recipesList)
  return recipes

@api.route("/submitrecipe", endpoint="submitrecipe")
class submitRecipe(Resource):
  def post(self):
    """ 
    Obtain recipe data from HTML form on the submission page \
    and posts the data to the corresponding tables in the \
    MySQL database.
    """
    try:
      form = flask.request.form
      recipe_title = form.getlist('recipe_title')[0]
      recipe_desc = form.getlist('recipe_desc')[0]
      total_time = form.getlist('total_time')[0]
      serving_size = form.getlist('serving_size')[0]
      ing_names = form.getlist('ing_name')
      ing_quants = form.getlist('ing_quant')
      ing_units = convertUnits(form.getlist('ing_units'))
      steps = form.getlist('steps')
      
      ingredients = []
      for i in range(len(ing_names)):
        ingredients.append((ing_names[i], ing_quants[i], ing_units[i]))
      
      # Post recipe to db
      custom_recipe = Recipe(name=recipe_title, description=recipe_desc, \
        totalTime=total_time, author=2, servingSize=serving_size)
      db.session.add(custom_recipe)
      db.session.commit()

      # Obtain autogenerated RecipeID through query
      rID = Recipe.query.filter_by(name=recipe_title, description=recipe_desc, \
        totalTime=total_time, author=2, servingSize=serving_size).first().RecipeID

      # Processing ingredients and quantities
      for ind, ingredient in enumerate(ing_names):
        # Check if ingredient exists and obtain IngredientID
        exist = Ingredient.query.filter_by(name=ingredient).first()
        if exist is None: # Post ingredient to db
          ingModel = Ingredient(name=ingredient)
          db.session.add(ingModel)
          db.session.commit()
          iID = Ingredient.query.filter_by(name=ingredient).first().IngredientID
        else:
          iID = exist.IngredientID
        # Post quantities to db
        quantModel = Quantity(value=ing_quants[ind], measurement=ing_units[ind], QRecipeID=int(rID), QIngredientID=int(iID))
        db.session.add(quantModel)
        db.session.commit()
      
      # Post steps to db
      for ind, step in enumerate(steps):
        stepModel = Steps(StepsRecipeID=rID, order=ind, direction=step)
        db.session.add(stepModel)
        db.session.commit()
      return flask.redirect("http://localhost:3000/Add")

    except Exception as e:
      print(e)
      return flask.redirect("http://localhost:3000")

@api.route("/displaycards", endpoint="displaycards")
class displaycards(Resource):
  def get(self):
    """ 
    Grabs custom recipes (user submitted) \
    from database and formatted for display.
    """
    recipes = Recipe.query.filter_by(author=2).all()
    numRecipes = len(recipes)
    recipes = formatRecipes(recipes)
    return {
      'num_recipes': numRecipes,
      'recipes': recipes
    }

@api.route("/searchrecipe", endpoint="searchrecipe")
@api.param('searchStr', 'Ingredient to search')
class searchRecipe(Resource):
  def get(self):
    """
    Accepts a query parameter search ingredient and returns \
    a list of recipes that contain the ingredient. The list \
    of recipes is formatted and sorted by lowest total time.
    """
    # Obtain search string query parameter
    args = flask.request.args
    search = args['searchStr']

    # Query for ingredient in database
    ing = Ingredient.query.filter_by(name=search).first()
    if ing is not None:
      iID = ing.IngredientID
    else:
      return {
        'num_recipes': 0,
        'recipes': []
      }

    # Query quantities for recipe IDs to return matching recipes
    quants = Quantity.query.filter_by(QIngredientID=iID).all()
    recipeIDs = set()
    for quant in quants:
      recipeIDs.add(quant.QRecipeID)
    recipes = []
    for rID in recipeIDs:
      recipe = Recipe.query.filter_by(RecipeID=rID).first()
      recipes.append(recipe)
    numRecipes = len(recipes)
    recipes = formatRecipes(recipes)
    return {
      'num_recipes': numRecipes,
      'recipes': recipes
    }

def main():
  app.run()

if __name__ == '__main__':
  main()