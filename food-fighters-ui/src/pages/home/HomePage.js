import './HomePage.css';
import '../../App.css';

import RecipeCard from './RecipeCard';
import React, {useState, useEffect} from 'react';
import axios from 'axios'
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import {ThemeProvider} from '@mui/material/styles';
import {theme} from '../../ColorTheme';

export default function HomePage() {
  const [values, setValues] = useState({
    search_string: ''
  });

  let [numRecipes, setNumRecipes] = useState(null);
  let [recipeList, setRecipeList] = useState(null);
  let [didSearch,  setDidSearch]  = useState(false);

  useEffect(() => {
    const article = { title: 'React Hooks POST Request Example' };
    axios.post('/displayrecipes', article)
        .then(response => {
          setNumRecipes(response.data.numRecipes);
          setRecipeList(response.data.recipeList)
        });
  }, []);

  // useEffect(() => {
  //   // POST request using axios inside useEffect React hook
  //   const article = { title: 'React Hooks POST Request Example' };
  //   axios.post('https://reqres.in/api/articles', article)
  //       .then(response => setArticleId(response.data.id));

  // // empty dependency array means this effect will only run once (like componentDidMount in classes)
  // }, []);

  const handleChange = (prop) => (event) => {
    setValues({ ...values, [prop]: event.target.value });
  };

  const handleSubmit = () => {
    setDidSearch(true);
  };

  return (
    <div className='homePage'>
      <ThemeProvider theme={theme}>
        <div className='homeHeader'>
          <h1>Welcome to Food Fighters!</h1>
        </div>
        <form action='searchrecipe' method='post'>
          <div className='recipeSearch'>
            <TextField
              label='Search For Recipes'
              placeholder='Type Ingredients'
              value={values.search_string}
              onChange={handleChange('search_string')}
              onSubmit={handleSubmit}
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
          {getCards(numRecipes, recipeList)}
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
