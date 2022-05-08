import React from 'react'
import Card from '@mui/material/Card';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import SimpleDialog from './Dialog';
import './RecipeCard.css';

// Recipe card to show some details about the listed recipe
export default function RecipeCard({recipe_name, ingredients, prep_time}) {
  const [open, setOpen] = React.useState(false);

  // Handle click on recipe card
  const handleClickOpen = () => {
    setOpen(true);
  };

  // Handle closing of recipe card
  const handleClose = () => {
    setOpen(false);
  };

  return (
    <Card variant="outlined" sx={{ height: 250, width: 300 }} id='Card'>

      <Typography gutterBottom variant="h5" component="div">
        <b>{recipe_name}</b>
      </Typography>

      <Typography variant="body2" color="text.secondary" component="div">
        <b>Prep Time:</b> {prep_time} minutes
      </Typography>

      <Typography variant="body2" color="text.secondary" component="div">
        <b>Ingredients:</b>
        <ul>
          {ingredients.map((ingredient, i) => {
            if (i >= 0 && i <= 2) {
              return (
                <li key={i}>
                  {ingredient}
                </li>
              );
            }
            else {
              return (
                <div key={i}></div>
              );
            }
          })}
          <li>
            ...
          </li>
        </ul>
      </Typography>

      <div className='container'></div>
      
      <Button
        className='detailsBtn'
        size="small"
        onClick={handleClickOpen}
      >
        Details
      </Button>

      <SimpleDialog
        open={open}
        onClose={handleClose}
        selectedRecipe={[recipe_name, ingredients, prep_time]}
      />

    </Card>
  );
}
