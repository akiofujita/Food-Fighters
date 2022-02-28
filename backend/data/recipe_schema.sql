PRAGMA foreign_keys = 1;

CREATE TABLE IF NOT EXISTS recipes (
  recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
  recipe_name TEXT NOT NULL,
  ingredients TEXT NOT NULL,
  prep_time INT NOT NULL, -- Consider changing to total time, add prep and cooking columns
  steps TEXT NOT NULL,
  poster_id INT NOT NULL
);

-- CREATE TABLE IF NOT EXISTS instructions (
--   FOREIGN KEY (recipe_id)
--     REFERENCES recipes (recipe_id)
-- )

-- Example entries for testing API
INSERT INTO recipes (recipe_name, ingredients, prep_time, steps, poster_id)
VALUES
( "Homemade Eggnog",
  "6 large egg yolks, 1/2 cup granulated sugar, 1 cup heavy whipping cream, 2 cups milk, 1/2 teaspoon ground nutmeg, pinch of salt, 1/4 teaspoon vanilla extract, ground cinnamon (for topping), alcohol (optional)",
   25,
   "1. Whisk the egg yolks and sugar together in a medium bowl until light and creamy.
    2. In a saucepan over medium-high heat, combine the cream, milk, nutmeg, and salt. Stir often until mixture reaches a bare simmer.
    3. Add a big spoonful of the hot milk to the egg mixture, whisking vigorously. Repeat, adding a big spoonful at a time, to temper the eggs.
    4. Once most of the hot milk has been added to the eggs, pour the mixture back into the saucepan on the stove.
    5. Whisk constantly for just a few minutes, until the mixture is just slightly thickened (or until it reaches about 160 degrees F on a thermometer). It will thicken more as it cools.
    6. Remove from heat and stir in the vanilla, and alcohol, if using.
    7. Pour the eggnog through a fine mesh strainer into a pitcher or other container and cover with plastic wrap.
    8. Refrigerate until chilled. It will thicken as it cools. If you want a thinner, completely smooth consistency, you can add the entire mixture to a blender with 1 or 2 tablespoons of milk and blend until smooth.
    9. Serve with a sprinkle of cinnamon or nutmeg, and fresh whipped cream, if desired.
    10. Store homemade eggnog in the fridge for up to one week.",
    -1 ),
( "Fried Rice Restaurant Style",
  "2 cups enriched white rice, 4 cups water, 2/3 cup chopped baby carrots, 1/2 cup frozen green peas, 2 tablespoons vegetable oil, 2 eggs, soy sauce (to taste), 2 tablespoons sesame oil (to taste)",
  45,
  "1. In a saucepan, combine rice and water. Bring to a boil. Reduce heat, cover, and simmer for 20 minutes.
  2. In a small saucepan, boil carrots in water about 3 to 5 minutes. Drop peas into boiling water, and drain.
  3. Heat wok over high heat. Pour in oil, then stir in carrots and peas; cook about 30 seconds. Crack in eggs, stirring quickly to scramble eggs with vegetables. Stir in cooked rice. Shake in soy sauce, and toss rice to coat. Drizzle with sesame oil, and toss again.",
  -1 ),
( "3am Chicken",
  "1 shallot or small onion, 2 stalks green onion, 3 garlic cloves (or to preference), 1 tbsp cumin, 1 tbsp coriander, 1 tbsp Szechuan pepper, 2-3 tbsp five spice powder, 1 tbsp smoked paprika (to taste), 1/4 cup all purpose flour",
  60,
  "1. Preheat oven to 400 degrees F.
   2. Add olive oil to pan, lightly fry diced onion/shallot, diced green onions, and diced garlic.
   3. Season chicken thighs with salt on both sides. Thoroughly coat chicken in flour mixed with spices.
   4. Extract onions and garlic from oil, reserve in small bowl. Season with salt and smoked paprika.
   5. Turn heat up to high, aggressively fry chicken skin side down until golden brown and crispy.
   6. Flip chicken so skin side is up. Put pan in oven and cook until 180-185 degrees F internal.
   7. (Optional) When chicken is around 165 degrees F, add green onion stalks in pan and lightly salt.
   8. Serve with rice.",
  -1 );