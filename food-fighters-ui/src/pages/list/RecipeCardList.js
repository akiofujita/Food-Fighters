import './RecipeCardList.css';
import React, {useState, useEffect} from 'react';
import RecipeCard from './RecipeCard';

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
        {getCards(numRecipes, recipeList)}
      </div>
    </div>
  );
}

function getCards(numRecipes, recipes) {
  const cardList = [];
  if (recipes) {
    for (var i = 0; i < numRecipes; i++) {
      cardList.push(<RecipeCard
        recipe_name={recipes[i][0]}
        ingredients={recipes[i][1]}
        prep_time={recipes[i][2]} />)
    }
  }
  return cardList;
}
