import './RecipeCard.css';

import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
// import CardMedia from '@mui/material/CardMedia';
// import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export default function RecipeCard({recipe_name, ingredients, prep_time}) {
  return (
    <Card variant="outlined" sx={{ maxWidth: 345 }} id='Card'>
      {/* <CardMedia
        component="img"
        alt="green iguana"
        height="140"
        image="/static/images/cards/contemplative-reptile.jpg"
      /> */}
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          <b>{recipe_name}</b>
        </Typography>
        <Typography variant="body2" color="text.secondary">
          <b>Prep Time:</b> {prep_time} minutes
        </Typography>
        <Typography variant="body2" color="text.secondary">
          <b>Ingredients:</b> {ingredients}
        </Typography>
      </CardContent>
      {/* <CardActions>
        <Button size="small">Details</Button>
      </CardActions> */}
    </Card>
  );
}
