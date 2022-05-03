import React from 'react';
import InputAdornment from '@mui/material/InputAdornment';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import {ThemeProvider} from '@mui/material/styles';
import {theme} from '../../ColorTheme';
import IngredientForm from './IngredientForm';
import StepForm from './StepForm';
import './InputForm.css';

export default function InputForm() {
  const [values, setValues] = React.useState({
    recipe_title: '',
    recipe_desc: '',
    total_time: null,
    serving_size: null
  });

  const handleChange = (prop) => (event) => {
    setValues({ ...values, [prop]: event.target.value });
  };
  
  return (
    <form className='recipeForm' action='submitrecipe' method='post'>
      <h2>Add New Recipe</h2>
      <ThemeProvider theme={theme}>
      <div className='recipeDetails'>
        <TextField
          required
          label='Recipe Title'
          value={values.recipe_title}
          onChange={handleChange('recipe_title')}
          name='recipe_title'
          id='recipe_title'
          sx={{
            mt: 2
          }}
        />
        <TextField
          label='Description'
          value={values.recipe_desc}
          onChange={handleChange('recipe_desc')}
          name='recipe_desc'
          id='recipe_desc'
          sx={{
            mt: 2
          }}
        />
        <div className='timeDetails'>
          <TextField
            required
            label='Total Time'
            name='total_time'
            id='total_time'
            value={values.total_time ? values.total_time : '' }
            onChange={handleChange('total_time')}
            sx={{
              mt: 2,
              mr: 2,
              minWidth: '40%'
            }}
            InputProps={{
              inputMode: 'numeric',
              pattern: '[0-9]*',
              endAdornment: <InputAdornment position='end'>minutes</InputAdornment>
            }}
          />
          <TextField
            required
            label='Serving Size'
            name='serving_size'
            id='serving_size'
            value={values.serving_size ? values.serving_size : '' }
            onChange={handleChange('serving_size')}
            sx={{
              mt: 2,
              mr: 2,
              minWidth: '40%'
            }}
          />
        </div>
      </div>
      <IngredientForm />
      <StepForm />
        <Button
          variant='outlined'
          type='submit'
          id='submitBtn'
        >
          Submit
        </Button>
      </ThemeProvider>
    </form>
  );
}
