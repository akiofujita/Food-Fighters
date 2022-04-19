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

# Writing to csv
recipe = ['name', 'time', 'servingSize']
ingredients = ['name', 'state', 'value', 'measurement']
steps = ['order', 'direction']
table_r = 'recipe.csv'
table_i = 'ingredient.csv'
table_s = 'steps.csv'

# Get rows
rows = []
bigingredient = ''
count = 0
for ingredient in scraper.ingredients():
    bigingredient += ingredient.replace(',', '/')
    count += 1
    if count != len(scraper.ingredients()):
        bigingredient += '\n'
instructions = scraper.instructions().replace(',', '/')
serving = scraper.yields().replace('serving(s)', '')[:-1]
row = [scraper.title(), scraper.total_time(), bigingredient, serving, instructions]
rows.append(row)

with open(filename, 'w') as csvfile:
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)