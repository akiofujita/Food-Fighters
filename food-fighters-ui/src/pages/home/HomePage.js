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
    console.log("use effect");
    const fetchData = async () => {
      if (searchStr !== "") {
        console.log("fetching...");
        // const myData = {
        //   search_string: searchStr
        // }
        // console.log("myData: " + JSON.stringify(myData));
        // const result = await fetch('/searchrecipe', {
        //   method: 'POST',
        //   headers: {
        //     'Content-Type': 'application/json'
        //   },
        //   body: JSON.stringify(myData)
        // })
        fetch('/searchrecipe/' + searchStr)
        .then(response => response.json())
        .then(data => {
          setRecipeRes({numRecipes: data.num_recipes, recipeList: data.recipes});
        });
        console.log("json");
        // const resultInJson = await result.json();
        // console.log(JSON.stringify(resultInJson));
      }
    }

    fetchData();
  }, [searchStr]);

  // useEffect(() => {
  //   // POST request using axios inside useEffect React hook
  //   const article = { title: 'React Hooks POST Request Example' };
  //   axios.post('https://reqres.in/api/articles', article)
  //       .then(response => setArticleId(response.data.id));

  // // empty dependency array means this effect will only run once (like componentDidMount in classes)
  // }, []);

  function handleChange(event) {
    setSearchStr(event.target.value);
    // setSearch( event.target.value );
  }

  return (
    <div className='homePage'>
      <ThemeProvider theme={theme}>
        <div className='homeHeader'>
          <h1>Welcome to Food Fighters!</h1>
        </div>
        <form>
          <div className='recipeSearch'>
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
            <IconButton id='searchIcon' type="submit" sx={{ p: '10px' }} aria-label="search">
              <SearchIcon />
            </IconButton>
          </div>
        </form>
        <div className='cards'>
          {getCards(recipeRes.numRecipes, recipeRes.recipeList)}
        </div>
      </ThemeProvider>
      <p>Did Search: {JSON.stringify(didSearch)}</p>
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
