import RecipeCard from './RecipeCard';
import React, {useState, useEffect} from 'react';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import ClipLoader from 'react-spinners/ClipLoader'
import {ThemeProvider} from '@mui/material/styles';
import {theme} from '../../ColorTheme';
import './HomePage.css';
import '../../App.css';

// Home and recipe search page!
export default function HomePage() {
  let [searchStr,  setSearchStr]  = useState("");
  let [recipeRes,  setRecipeRes]  = useState({
    numRecipes: null,
    recipeList: null
  });
  let [searchCount,  setSearchCount] = useState(0);
  let [isLoading,    setIsLoading  ] = useState(false);
  let [noResults,    setNoResults  ] = useState(false);

  // Update status of loading or getting no results
  useEffect(() => {
    if (recipeRes.numRecipes > 0 && recipeRes.recipeList) {
      setIsLoading(false);
      setNoResults(false);
    }
    else if (recipeRes.numRecipes === -1) {
      setIsLoading(false);
      setNoResults(true);
    }
  }, [recipeRes])

  // Handle change in the typed search string
  function handleChange(event) {
    setSearchStr(event.target.value);
  }

  // Handle submission of the search
  function handleSubmit(event) {
    event.preventDefault();
    setSearchCount(searchCount + 1);

    const fetchData = async () => {
      if (searchStr !== "") {
        setIsLoading(true);
        setNoResults(false);
        fetch('/searchrecipe?searchStr=' + searchStr)
        .then(response => response.json())
        .then(data => {
          setRecipeRes({numRecipes: data.num_recipes, recipeList: data.recipes});
          if(searchCount === 0) {
            setSearchCount(searchCount + 1);
          }
        });
      }
    }

    fetchData();
  }

  return (
    <div className='homePage'>
      <ThemeProvider theme={theme}>
        
        {searchCount === 0 &&
          <div className='homeHeader'>
            <h1>Welcome to Food Fighters!</h1>
          </div>
        }

        <form onSubmit={handleSubmit}>
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

        <div className='results'>
          <div className='clip'>
            <ClipLoader loading={isLoading} color={'#43af2a'}/>
          </div>
          <div className='noResults'>
            {noResults && <h4>No Results Found</h4>}
          </div>
          <div className='cards'>
            {recipeRes.numRecipes > 0 && recipeRes.recipeList &&
            recipeRes.recipeList.map((recipe, i) => {
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

      </ThemeProvider>
    </div>
  );
};
