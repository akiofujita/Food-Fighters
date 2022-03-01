import './RecipeCardList.css';
import React, {useState, useEffect} from 'react';
import RecipeCard from './RecipeCard';

export default function RecipeCardList() {
  let [recName,    setRecName   ] = useState(null);
  let [recIng,     setRecIng    ] = useState(null);
  let [recTime,    setRecTime   ] = useState(null);

  useEffect(() => {
    fetch('/getcard')
    .then(response => response.json())
    .then(data => {
      setRecName(data.recipe_name);
      setRecIng(data.ingredients);
      setRecTime(data.prep_time);
    });
  }, []);

  return (
    <div className='recipeCardList'>
      <RecipeCard
      recipe_name={recName}
      ingredients={recIng}
      prep_time={recTime} />
    </div>
  );
}
