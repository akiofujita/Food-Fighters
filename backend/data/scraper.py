from fileinput import filename
from recipe_scrapers import scrape_me
import mysql.connector
from unicodedata import numeric
import re
import sys
import csv


units = ['ounces', 'ounce', 'oz', 'pounds', 'pound', 'lb', 'lbs', 'gallons', 'gallon', 'gal', 'quarts', 
         'quart', 'qt', 'pints', 'pint', 'cups', 'cup', 'tablespoons', 'tablespoon', 'tbsp', 'tsp', 
         'teaspoons', 'teaspoon', 'fluid ounce', 'fluid ounces', 'fl. oz', 'liters', 'liter', 'pinches', 
         'pinch', 'cloves', 'clove']

class Recipe:
  def __init__(self, name, time, servingSize, user):
    self.name = name
    self.time = time
    self.servingSize = servingSize
    self.user = user

class Ingredient:
  def __init__(self, value, measurement, name, state):
    self.value = value
    self.measurement = measurement
    self.name = name
    self.state = state
    
class Step:
  def __init__(self, order, direction):
    self.order = order
    self.direction = direction

def convert_to_float(frac_str):
  """
  Args:
      frac_str (string): the string that needs to be converted into a float

  Returns:
      float: the float equivalent of the original string
  """
  if len(frac_str) == 0:
      return ''

  # Special case if it's not unicode
  if '/' in frac_str:
    num, denom = frac_str.split('/')
    try:
      leading, num = num.split(' ')
      whole = float(leading)
    except ValueError:
      whole = 0
    frac = float(num) / float(denom)
    v = whole - frac if whole < 0 else whole + frac

  elif len(frac_str) == 1:
    v = numeric(frac_str)
  elif frac_str[-1].isdigit():
    # normal number, ending in [0-9]
    v = float(frac_str)
  else:
    # Assume the last character is a vulgar fraction
    v = float(frac_str[:-1]) + numeric(frac_str[-1])
  return v

def scrape(scraper):
  """
  Args:
    scraper (scrape_me object): raw data obtained from recipe_scrapers

  Returns:
    Recipe: Recipe object
    Ingredients: list of Ingredient objects
    Steps: list of Steps objects 
  """
  # Get recipe data
  serving = re.findall(r'\d+', scraper.yields())[0]
  recipe = Recipe(scraper.title(), scraper.total_time(), serving, 1)

  # Get ingredient data
  ingredients = []
  for ingredient in scraper.ingredients():
    p_value = '1'
    value = ''
    
    # First, get parenthesis info i.e. 1 (7 ounce can) or 6 (9 inch) tortillas
    parenthesis = r"(?i)\((.*?)\)"
    in_parenthesis = re.findall(parenthesis, ingredient)
    if len(in_parenthesis) > 0:
      # If match is found, then check units
      is_units = in_parenthesis[0].split(' ')[-1]
      # If units match, then this is the unit and hold onto the number for multiplication
      if is_units in units:
        p_value = re.findall(r'((\d*\ *\d+/\d+)|([.]?\d+))', in_parenthesis[0])[0]
        measurement = is_units
        # Also get rid of the parenthesis from the ingredient string as well as the container
        ingredient = re.sub(r"\([^()]*\)", "", ingredient, 1)
        ingredient = ingredient.split('  ')[0] + '  ' + ingredient.split('  ')[1].split(' ', 1)[1]
  
    # Then, look for numerical value (this includes fractions and unicode)
    if len(re.findall(r'(?u)((\d*\ ?[\u00BC-\u00BE\u2150-\u215E]+)|(\d*\ *\d+/\d+)|([.]?\d+))'
                      , ingredient)) > 0:
      # Multiply by p_value (default is 1, but will change if there are values in parenthesis)
      value = re.findall(r'(?u)((\d*\ ?[\u00BC-\u00BE\u2150-\u215E]+)|(\d*\ *\d+/\d+)|([.]?\d+))', 
                                              ingredient)[0][0]
      value = str(convert_to_float(value)*convert_to_float(p_value[0]))
      # Get rid of number now that we have that
      ingredient = re.sub(r"(?u)((\d*\ ?[\u00BC-\u00BE\u2150-\u215E]+)|(\d*\ *\d+/\d+)|([.]?\d+))", ""
                          , ingredient, 1)[1:]

    state = ''
    # Get state which is always indicated by the comma
    if ',' in ingredient:
      state = ingredient.split(',')[-1]
      ingredient = ingredient[:ingredient.rfind(',')]

    # Check for measurement at all
    measurement = ''
    name = ingredient
    split = ingredient.split(' ')
    if len(split) > 1:
      if split[0] in units:
        if split[0] == 'fluid':
          measurement = split[0] + ' ' + split[1]
          name = ingredient.replace(measurement, '')[1:]
        else:
          measurement = split[0]
          name = ingredient.replace(measurement, '')[1:]
    ingredients.append(Ingredient(value, measurement, name.strip(), state))

  # Getting steps
  steps = []
  instructions = scraper.instructions().split('\n')
  count = 1
  for instruction in instructions:
    steps.append(Step(count, instruction))
    count += 1
  
  return recipe, steps, ingredients
        
  
def write_to_db (recipe, steps, ingredients):
  """
  Args:
    scraper (scrape_me object): raw data obtained from recipe_scrapers

  Returns:
    Recipe: Recipe object
    Ingredients: list of Ingredient objects
    Steps: list of Steps objects 
  """
  conn = mysql.connector.connect(user='root', password='F00D_fighters22', host = 'localhost', database='foodfighters')
  cursor = conn.cursor(buffered=True)
  
  cursor.execute(
      "INSERT INTO recipe (name,totalTime,servingSize,author) VALUES (%s, %s, %s, %s)", 
      [recipe.name, recipe.time, recipe.servingSize, recipe.user])
  # Get RecipeID from newly generated row
  cursor.execute("SELECT RecipeID FROM foodfighters.recipe WHERE name = %s", [recipe.name])
  RecipeID = cursor.fetchone()[0]

  for step in steps:
    cursor.execute(
        "INSERT INTO steps (StepsRecipeID, steps.order, direction) VALUES (%s, %s, %s)", 
        [RecipeID, step.order, step.direction])

  for ingredient in ingredients:
    # CHECK FOR DUPLICATES FIRST
    cursor.execute("SELECT COUNT(name) FROM ingredient WHERE name = %s", [ingredient.name])
    count = cursor.fetchone()[0]
    # Only insert if there are no duplicates (aka it's unique)
    if count == 0:
      cursor.execute(
          "INSERT INTO ingredient (name) VALUES (%s)", [ingredient.name])

    # Get IngredientID
    # If value is a fraction
    convert_val = convert_to_float(ingredient.value)
    ingredient.value = convert_val

    cursor.execute("SELECT IngredientID FROM foodfighters.ingredient WHERE name = %s", [ingredient.name])
    IngredientID = cursor.fetchone()[0]

    # Insert quantity
    if ingredient.value == '':
      cursor.execute(
      "INSERT INTO quantity (QRecipeID, QIngredientID, measurement, state) VALUES (%s, %s, %s, %s)",
      [RecipeID, IngredientID, ingredient.measurement, ingredient.state])
    else:
      cursor.execute(
          "INSERT INTO quantity (QRecipeID, QIngredientID, value, measurement, state) VALUES (%s, %s, %s, %s, %s)"
          , [RecipeID, IngredientID, ingredient.value, ingredient.measurement, ingredient.state])
  conn.commit()
  cursor.close()


def main():
  args = sys.argv[1:]
  if len(args) == 0:
    sys.exit("Please enter an allrecipes.com link or a .csv file name.")

  allrecipe = r"(?i)\b((?:https?://|www[.]|(allrecipes[.]com/recipe/+[0-9]{5,6})|[\w\d-]*))"
  isvalid = re.compile(allrecipe)
  
  # Case 1: .csv file
  if '.csv' in sys.argv[1]:
    with open(sys.argv[1], 'r') as csvfile:
      datareader = csv.reader(csvfile)
      for link in datareader:
        scraper = scrape_me(link[0])
        recipe, steps, ingredients = scrape(scraper)
        write_to_db(recipe, steps, ingredients)
    sys.exit("Done")
      
  # Case 2: allrecipes.com  
  elif re.search(isvalid, sys.argv[1]):
    scraper = scrape_me(sys.argv[1])
    recipe, steps, ingredients = scrape(scraper)
    write_to_db(recipe, steps, ingredients)
    sys.exit("Done")

  else:
    sys.exit("Not a valid allrecipes.com link or a .csv file path.")


if __name__=="__main__":
  main()