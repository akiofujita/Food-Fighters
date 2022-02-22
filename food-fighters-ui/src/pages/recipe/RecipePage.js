import './RecipePage.css';
import '../../App.css';
import { useState } from 'react'
import axios from "axios";

export default function RecipePage() {
  let [recipe, setRecipe] = useState(null);

  function getData() {
    axios({
      method: "GET",
      url:"/display",
    })
    .then((response) => {
      const res =response.data
      setRecipe(({
        recipe_name: res.recipe_name}))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

  return (
    <div className='recipePage'>
      <h2>Recipe Page</h2>
      <div className='break'/>

      <p>Get Recipe </p><button onClick={getData}>Click me</button>
      {recipe && <div>
          <p>Fetched Recipe: {recipe.recipe_name}</p>
        </div>
      }
    </div>
  );
};