import './HomePage.css';
import '../../App.css';

import RecipeCard from './RecipeCard';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import {ThemeProvider} from '@mui/material/styles';
import {theme} from '../../ColorTheme';
import {useSearchParams} from 'react-router-dom';

export default function HomePage() {
  let [searchStr,  setSearchStr]  = useState("");
  let [recipeRes,  setRecipeRes]  = useState({
    numRecipes: null,
    recipeList: null
  })
  let [didSearch,  setDidSearch]  = useState(false);

  const [search, setSearch] = useSearchParams();

  useEffect(() => {
    const fetchData = async () => {
      if (searchStr !== "") {
        fetch('/searchrecipe?searchStr=' + searchStr)
        .then(response => response.json())
        .then(data => {
          setRecipeRes({numRecipes: data.num_recipes, recipeList: data.recipes});
        });
        setDidSearch(true);
      }
    }

    fetchData();
  }, [searchStr]);

  function handleChange(event) {
    setSearchStr(event.target.value);
  }

  return (
    <div className='homePage'>
      <ThemeProvider theme={theme}>
        {!didSearch &&
          <div className='homeHeader'>
            <h1>Welcome to Food Fighters!</h1>
          </div>
        }
        <form>
          <div className='recipeSearch'>
            <div className='searchBox'>
              <TextField
                label='Search For Recipes'
                placeholder='Type Ingredients'
                value={searchStr}
                onChange={handleChange}
                name='search_string'
                id='search_string'
                sx={{
                  mt: 2
                }}
              />
            </div>
            <IconButton id='searchIcon' type="submit" sx={{ p: '10px' }} aria-label="search">
              <SearchIcon />
            </IconButton>
          </div>
        </form>
        <div className='cards'>
          {getCards(recipeRes.numRecipes, recipeRes.recipeList)}
        </div>
      </ThemeProvider>
    </div>
  );
};

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