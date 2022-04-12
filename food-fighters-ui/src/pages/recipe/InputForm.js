import './InputForm.css';
import React, {useState, useEffect} from 'react';
import Box from '@mui/material/Box';
import Input from '@mui/material/Input';
import FilledInput from '@mui/material/FilledInput';
import OutlinedInput from '@mui/material/OutlinedInput';

import InputAdornment from '@mui/material/InputAdornment';
import FormHelperText from '@mui/material/FormHelperText';
import FormControl from '@mui/material/FormControl';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogActions from '@mui/material/DialogActions';
import Button from '@mui/material/Button';
import Autocomplete, { createFilterOptions } from '@mui/material/Autocomplete';
import MenuItem from '@mui/material/MenuItem';
import IngredientForm from './IngredientForm';
import {ThemeProvider} from '@mui/material/styles';
import {theme} from './ColorTheme'
import StepForm from './StepForm'
// import axios from 'axios';
// import Visibility from '@mui/icons-material/Visibility';
// import VisibilityOff from '@mui/icons-material/VisibilityOff';

export default function InputForm() {
  const [values, setValues] = React.useState({
    recipe_title: '',
    recipe_desc: '',
    prep_time: null,
    cook_time: null,
  });

  const handleChange = (prop) => (event) => {
    setValues({ ...values, [prop]: event.target.value });
  };
  
  return (
    <form className='recipeForm' action="submitrecipe" method="post">
      <h2>Add New Recipe</h2>
      <div className='recipeDetails'>
        <TextField
          required
          label="Recipe Title"
          value={values.recipe_title}
          onChange={handleChange('recipe_title')}
          name="recipe_title"
          id="recipe_title"
          sx={{
            mt: 2
          }}
        />
        <TextField
          label="Description"
          value={values.recipe_desc}
          onChange={handleChange('recipe_desc')}
          name="recipe_desc"
          id="recipe_desc"
          sx={{
            mt: 2
          }}
        />
        <div className="timeDetails">
          <TextField
            required
            label="Prep Time"
            name="prep_time"
            id="prep_time"
            value={values.prep_time}
            onChange={handleChange('prep_time')}
            sx={{
              mt: 2,
              mr: 2,
              minWidth: '40%'
            }}
            InputProps={{
              inputMode: 'numeric',
              pattern: '[0-9]*',
              endAdornment: <InputAdornment position="end">minutes</InputAdornment>
            }}
          />
          <TextField
            required
            label="Cook Time"
            name="cook_time"
            id="cook_time"
            value={values.cook_time}
            onChange={handleChange('cook_time')}
            sx={{
              mt: 2,
              minWidth: '40%'
            }}
            InputProps={{
              inputMode: 'numeric',
              pattern: '[0-9]*',
              endAdornment: <InputAdornment position="end">minutes</InputAdornment>
            }}
          />
        </div>
      </div>
      <IngredientForm />
      <StepForm />
      <ThemeProvider theme={theme}>
        <Button
          variant="outlined"
          type="submit"
          id="submitBtn"
        >
          Submit
        </Button>
      </ThemeProvider>
    </form>
  );
}
