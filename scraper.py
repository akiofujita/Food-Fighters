from fileinput import filename
from recipe_scrapers import scrape_me
import mysql.connector
from unicodedata import numeric
import csv 
import sys

units = ['ounces', 'ounce', 'pounds', 'pound', 'gallons', 'gallon', 'quarts', 'quart', 'pints', 'pint', 'cups', 'cup', 'tablespoons', 'tablespoon', 'teaspoons', 'teaspoon', 'fluid', 'liters', 'liter', 'pinches', 'pinch', 'cloves', 'clove'] 

# This is to remember what the indexes mean
# recipe = ['name', 'time', 'servingSize', 'user']
# ingredients = ['value', 'measurement','name', 'state']
# steps = ['order', 'direction']

def convert_to_float(frac_str):
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

def scrape_and_write(scraper):
    # Get recipe data
    serving = scraper.yields().split(' ')[0]
    recipe = [scraper.title(), scraper.total_time(), serving, 1]

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
            state = ingredient.split(',')[1]
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
        ingredients.append([value, measurement, name, state])

    # Getting steps
    steps = []
    instructions = scraper.instructions().split('\n')
    count = 1
    for instruction in instructions:
        steps.append([count, instruction])
        count += 1

    # Trying csv import via python
    conn = mysql.connector.connect(user='root', password='F00D_fighters22', host = 'localhost', database='foodfighters')

    cursor = conn.cursor(buffered=True)

    #print('Importing...')

    cursor.execute(
        "INSERT INTO recipe (name,totalTime,servingSize,author) VALUES (%s, %s, %s, %s)", recipe)
    # Get RecipeID from newly generated row
    #print(row[0])
    cursor.execute("SELECT RecipeID FROM foodfighters.recipe WHERE name = %s", [recipe[0]])
    RecipeID = cursor.fetchone()[0]
    #print(RecipeID)

    for row in steps:
        #print(row)
        cursor.execute(
            "INSERT INTO steps (StepsRecipeID, steps.order, direction) VALUES (%s, %s, %s)", [RecipeID, row[0], row[1]])

    for row in ingredients:
        #print(row)
        # CHECK FOR DUPLICATES FIRST
        cursor.execute("SELECT COUNT(name) FROM ingredient WHERE name = %s", [row[2]])
        count = cursor.fetchone()[0]
        #print(count)
        # Only insert if there are no duplicates (aka it's unique)
        if count == 0:
            cursor.execute(
                "INSERT INTO ingredient (name) VALUES (%s)", [row[2]])
        
        # Get IngredientID
        # If value is a fraction
        convert_val = convert_to_float(row[0])
        row[0] = convert_val
        
        cursor.execute("SELECT IngredientID FROM foodfighters.ingredient WHERE name = %s", [row[2]])
        IngredientID = cursor.fetchone()[0]
        #print(IngredientID)
        
        # Insert quantity
        if row[0] == '':
            cursor.execute(
            "INSERT INTO quantity (QRecipeID, QIngredientID, measurement, state) VALUES (%s, %s, %s, %s)", [RecipeID, IngredientID, row[1], row[3]])
        else:
            cursor.execute(
                "INSERT INTO quantity (QRecipeID, QIngredientID, value, measurement, state) VALUES (%s, %s, %s, %s, %s)", [RecipeID, IngredientID, row[0], row[1], row[3]])

    conn.commit()
    cursor.close()
    
def main():
    with open('toget.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for link in datareader:
            scraper = scrape_me(link[0])
            scrape_and_write(scraper)
            
if __name__=="__main__":
    main()
    print('Done')