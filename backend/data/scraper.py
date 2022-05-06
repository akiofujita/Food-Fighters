from fileinput import filename
from recipe_scrapers import scrape_me
import mysql.connector
from unicodedata import numeric
import re
import sys
import csv


units = ['ounces', 'ounce', 'pounds', 'pound', 'gallons', 'gallon', 'quarts', 
         'quart', 'pints', 'pint', 'cups', 'cup', 'tablespoons', 'tablespoon', 
         'teaspoons', 'teaspoon', 'fluid', 'liters', 'liter', 'pinches', 
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
  serving = scraper.yields().split(' ')[0]
  recipe = Recipe(scraper.title(), scraper.total_time(), serving, 1)

  # Get ingredient data
  ingredients = []
  for ingredient in scraper.ingredients():
      split = ingredient.split(' ')
      measurement = ''
      is_uni = False
      value = split[0]
      name_ind_start = 1
      print(ingredient)
      # If it's a string, where we grab ingredient name starts earlier
      if split[0][0].isalpha():
          # Check to see if it's actually just unicode
          if ord(split[0][0]) < 127:
          # character is ASCII, not unicode
              value = ''
              name_ind_start = 0

      # Check for unicode mixed numbers
      if len(split) > 1 and ord(split[1][0]) > 127:
          value += split[1]
          name_ind_start = 2
          is_uni = True

      state = ''
      name_ind_end = len(ingredient.split(',')[0].split(' '))
      # Get state which is always indicated by the comma
      if ',' in ingredient:
          state = ingredient.split(',')[-1]
          print(state)
      # Get the Real Measurement if there's parenthesis (aka 1 can = 7 oz)
      if '(' in ingredient and ingredient[ingredient.index('(')+1:ingredient.index('(')+2].isdigit():
          actual = ingredient[ingredient.index('(')+1:ingredient.index(')')]
          if actual.split(' ')[1] == 'fluid':
              value = str(convert_to_float(actual.split(' ')[0])*convert_to_float(ingredient.split(' ')[0]))
              measurement = actual.split(' ')[1] + actual.split(' ')[2]
              name_ind_start = 5
          elif actual.split(' ')[1] in units:
              value = str(convert_to_float(actual.split(' ')[0])*convert_to_float(ingredient.split(' ')[0]))
              measurement = actual.split(' ')[1]
              name_ind_start = 4
          # If parenthesis just don't mean that at all i.e. 10 (6 inch) corn tortillas

      # Otherwise check for if there's a measurement at all
      if len(split) > 1:
          if split[1] in units:
              if split[1] == 'fluid':
                  measurement = split[1] + ' ' + split[2]
                  name_ind_start = 3
              else:
                  measurement = split[1]
                  name_ind_start = 2
          elif len(split) > 2 and split[2] in units:
              if is_uni:
                  measurement = split[2]
                  name_ind_start = 3
                  if split[2] == 'fluid':
                      measurement = split[2] + ' ' + split[3]
                      name_ind_start = 4
      
      # Get the ingredient name
      name = ''
      for index in range(name_ind_start, name_ind_end):
          if ',' in ingredient.split(' ')[index]:
              name += ingredient.split(' ')[index][:-1] + ' '
          else:
              name += ingredient.split(' ')[index] + ' '
      print([value, measurement, name, state])
      ingredients.append(Ingredient(value, measurement, name, state))

  # Getting steps
  steps = []
  instructions = scraper.instructions().split('\n')
  count = 1
  for instruction in instructions:
      steps.append(Step(count, instruction))
      count += 1
  
  return recipe, ingredients, steps
        
  
def write_to_db (recipe, steps, ingredients):
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
      print("Please enter an allrecipes.com link or a .csv file name.")

  # Case 1: allrecipes.com link
  allrecipe = r"(?i)\b((?:https?://|www[.]|(allrecipes[.]com/recipe/+[0-9]{5,6})|[\w\d-]*))"
  isvalid = re.compile(allrecipe)
  if(re.search(isvalid, sys.argv[2])):
      scraper = scrape_me(sys.arvg[2])
      recipe, ingredients, steps = scrape(scraper)
      write_to_db(recipe, ingredients, steps)
      sys.exit("Done")

  # Case 2: .csv file
  elif '.csv' in sys.arvg[2]:
      with open(filename, 'r') as csvfile:
          datareader = csv.reader(csvfile)
          for link in datareader:
              scraper = scrape_me(link[0])
              recipe, ingredients, steps = scrape(scraper)
              write_to_db(recipe, ingredients, steps)
      sys.exit("Done")

  else:
      sys.exit("Not a valid allrecipes.com link or a .csv file path.")

if __name__=="__main__":
  main()