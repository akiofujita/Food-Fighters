from fileinput import filename
from recipe_scrapers import scrape_me
import csv 

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')

# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
# scraper = scrape_me('https://www.feastingathome.com/tomato-risotto/', wild_mode=True)

print(scraper.title())
print(scraper.total_time())
print(scraper.yields())
print(type(scraper.yields()))
print(scraper.ingredients())
print(scraper.instructions())
print(type(scraper.instructions()))

units = 'ounces pounds gallons quarts pints cups tablespoons teaspoons fluid ounces liters pinches cloves' 

# Writing to csv
recipe = ['name', 'time', 'servingSize']
ingredients = ['value', 'measurement','name', 'state']
steps = ['order', 'direction']
table_r = 'recipe.csv'
table_i = 'ingredient.csv'
table_s = 'steps.csv'

# Writing to recipe table
serving = scraper.yields().replace('serving(s)', '')[:-1]
rows_r = [[scraper.title(), scraper.total_time(), serving]]

with open('recipe.csv', 'w') as csvfile:
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(recipe) 
    # writing the data rows 
    csvwriter.writerows(rows_r)

# Writing to ingredient table
rows_i = []
for ingredient in scraper.ingredients():
    measurement = ''
    value = ingredient.split(' ')[0]
    state = ''
    name_ind_start = 1
    name_ind_end = len(ingredient.split(',')[0].split(' '))
    # Get state which is always indicated by the comma
    if ',' in ingredient:
        state = ingredient.split(',')[1]
        print(state)
    # Get the Real Measurement if there's parenthesis (aka 1 can = 7 oz)
    if '(' in ingredient:
        actual = ingredient[ingredient.index('(')+1:ingredient.index(')')]
        value = str(int(actual.split(' ')[0])*int(ingredient.split(' ')[0]))
        if actual.split(' ')[1] == 'fluid':
            measurement = actual.split(' ')[1] + actual.split(' ')[2]
        else:
            measurement = actual.split(' ')[1]
        name_ind_start = 4
        print(value)
        print(measurement)
    # Otherwise check for if there's a measurement at all
    if ingredient.split(' ')[1] in units:
        if ingredient.split(' ')[1] == 'fluid':
            measurement = ingredient.split(' ')[1] + ingredient.split(' ')[2]
            name_ind_start = 3
        else:
            measurement = ingredient.split(' ')[1]
            name_ind_start = 2
    # Get the ingredient name
    name = ''
    for index in range(name_ind_start, name_ind_end):
        if ',' in ingredient.split(' ')[index]:
            name += ingredient.split(' ')[index][:-1] + ' '
        else:
            name += ingredient.split(' ')[index] + ' '
    rows_i.append([value, measurement, name, state])
    
with open('ingredients.csv', 'w') as csvfile:
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(ingredients) 
    # writing the data rows 
    csvwriter.writerows(rows_i)

# Writing to steps
rows_s = []
instructions = scraper.instructions().split('\n')
count = 1
for instruction in instructions:
    rows_s.append([count, instruction])
    count += 1
    
with open('steps.csv', 'w') as csvfile:
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(steps) 
    # writing the data rows 
    csvwriter.writerows(rows_s)

