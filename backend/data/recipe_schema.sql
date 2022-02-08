CREATE TABLE IF NOT EXISTS recipes (
  recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
  recipe_name TEXT NOT NULL,
  ingredients TEXT NOT NULL,
  steps TEXT NOT NULL,
  poster_id INT NOT NULL
)