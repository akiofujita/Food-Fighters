SELECT * FROM recipe;
SELECT * FROM quantity;
SELECT * FROM steps;
SELECT * FROM ingredient;
# This is for resetting the database to only 5 sample manually-inputted recipes
DELETE FROM ingredient WHERE IngredientID >= 37;
DELETE FROM recipe WHERE RecipeID >= 6;
DELETE FROM quantity WHERE QRecipeID >= 6;