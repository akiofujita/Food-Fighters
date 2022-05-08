import React, {useState, useEffect} from 'react';
import RecipeCard from './RecipeCard';
import './RecipeCardList.css';

export default function RecipeCardList() {
  let [numRecipes, setNumRecipes] = useState(null);
  let [recipeList, setRecipeList] = useState(null);

  useEffect(() => {
    fetch('/displaycards')
    .then(response => response.json())
    .then(data => {
      setNumRecipes(data.num_recipes);
      setRecipeList(data.recipes);
    });
  }, []);

  return (
    <div className='recipeCardList'>
      <div className='cards'>
        {numRecipes > 0 && recipeList &&
         recipeList.map((recipe, i) => {
          return (
            <div key={i}>
              <RecipeCard
                recipe_name={recipe[0]}
                ingredients={recipe[1]}
                prep_time={recipe[2]}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
}
