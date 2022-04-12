import './InputForm.css';
import React, {useState, useEffect} from 'react';
import Box from '@mui/material/Box';
import Input from '@mui/material/Input';
import FilledInput from '@mui/material/FilledInput';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
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
import Select, { SelectChangeEvent } from '@mui/material/Select';
import IngredientForm from './IngredientForm';
import Bot from './bot'
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
    <div className='recipeForm'>
      {/* <Bot /> */}
      <div>
      <Box
        component="form"
        sx={{
          '& .MuiTextField-root': { m: 1, width: '75ch' },
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
          flexWrap: 'wrap',
          overflow: 'auto',
          // width: 20vw,
        }}
        noValidate
        autoComplete="off"
      >
        <TextField
          required
          label="Recipe Title"
          value={values.recipe_title}
          onChange={handleChange('recipe_title')}
          id="recipe_title"
        />
        <TextField
          label="Description"
          value={values.recipe_desc}
          onChange={handleChange('recipe_desc')}
          id="recipe_desc"
        />
      </Box>
      <Box
        component="form"
        sx={{
          '& .MuiTextField-root': { m: 1, width: '25ch' },
        }}
        noValidate
        autoComplete="off"
      >
        <TextField
          required
          label="Prep Time"
          id="outlined-adornment-weight"
          value={values.prep_time}
          onChange={handleChange('prep_time')}
          sx={{ m: 1, width: '30ch' }}
          InputProps={{
            inputMode: 'numeric',
            pattern: '[0-9]*',
            endAdornment: <InputAdornment position="end">minutes</InputAdornment>
          }}
        />
        <TextField
          required
          label="Cook Time"
          id="outlined-adornment-weight"
          value={values.cook_time}
          onChange={handleChange('cook_time')}
          sx={{ m: 1, width: '30ch' }}
          InputProps={{
            inputMode: 'numeric',
            pattern: '[0-9]*',
            endAdornment: <InputAdornment position="end">minutes</InputAdornment>
          }}
        />
      </Box>
      </div>
      <div>
        <IngredientForm />
      </div>
    </div>
  );
}

// class InputForm extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       val_recipe_title: "",
//       val_recipe_desc: "",
//       val_ingredients: "",
//       val_prep_time:   "",
//       val_steps:       "",
//       val_quant: "",
//       val_units: "",
//       open: false
//     };
//     this.handleChange = this.handleChange.bind(this);
//     this.handleClose = this.handleClose.bind(this);
//   }

//   handleChange(event) {
//     this.setState({
//       val_recipe_title: event.target.val_recipe_title,
//       val_recipe_desc:  event.target.val_recipe_desc,
//       val_ingredients:  event.target.val_ingredients,
//       val_prep_time:    event.target.val_prep_time,
//       val_steps:        event.target.val_steps,
//       val_units:        event.target.val_units
//     });
//   }

//   handleClose(event) {
//     this.setState()
//     this.state.open = false;
//   };

//   render() {
//     return (
//       <div className="inputForm">
//         <form action="submitrecipe" method="post">
//           <TextField
//             required
//             label="Recipe Title"
//             onChange={this.handleChange}
//             id="recipe_title"
//             sx={{ m: 1, width: '30ch' }}
//           />
//           <TextField
//             label="Description"
//             onChange={this.handleChange}
//             id="recipe_desc"
//             sx={{ m: 1, width: '30ch' }}
//           />
//           <TextField
//             required
//             label="Prep Time"
//             id="outlined-adornment-weight"
//             // value={values.weight}
//             onChange={this.handleChange}
//             sx={{ m: 1, width: '30ch' }}
//             InputProps={{
//               endAdornment: <InputAdornment position="end">minutes</InputAdornment>,
//             }}
//           />
//           <TextField
//             required
//             label="Cook Time"
//             id="outlined-adornment-weight"
//             // value={values.weight}
//             onChange={this.handleChange}
//             sx={{ m: 1, width: '30ch' }}
//             InputProps={{
//               endAdornment: <InputAdornment position="end">minutes</InputAdornment>,
//             }}
//           />
//           <h4>Add Ingredients</h4>
//           <div>
//             <Autocomplete
//               required
//               freeSolo
//               id="free-solo-2-demo"
//               disableClearable
//               sx={{ m: 1, width: '30ch' }}
//               options={top100Films.map((option) => option.title)}
//               renderInput={(params) => (
//                 <TextField
//                   {...params}
//                   label="Ingredient"
//                   InputProps={{
//                     ...params.InputProps,
//                     type: 'search',
//                   }}
//                 />
//               )}
//             />
//             <TextField
//               required
//               label="Quantity"
//               id="outlined-adornment-weight"
//               // value={values.weight}
//               onChange={this.handleChange}
//               sx={{ m: 1, width: '30ch' }}
//               inputProps={{
//                 inputMode: 'numeric',
//                 pattern: '[0-9]*'
//               }}
//             />
//             <FormControl fullWidth sx={{ m: 1, minWidth: 100 }} >
//               <InputLabel id="demo-simple-select-label">Units *</InputLabel>
//               <Select
//                 required
//                 label="Units"
//                 labelId="demo-simple-select-label"
//                 id="demo-simple-select"
//                 value={this.state.val_units}
//                 onChange={this.handleChange}
//               >
//                 <MenuItem value={1}>g</MenuItem>
//                 <MenuItem value={2}>tbsp</MenuItem>
//                 <MenuItem value={3}>pinch</MenuItem>
//               </Select>
//             </FormControl>
            
//           </div>
          

//           {/* <Autocomplete
//             // value={value}
//             onChange={(event, newValue) => {
//               if (typeof newValue === 'string') {
//                 // timeout to avoid instant validation of the dialog's form.
//                 // setTimeout(() => {
//                 //   toggleOpen(true);
//                 //   setDialogValue({
//                 //     title: newValue,
//                 //     year: '',
//                 //   });
//                 // });
//               } else if (newValue && newValue.inputValue) {
//                 this.state.open = true;
                
//               } else {
//                 this.state.val_ingredients = newValue;
//               }
//             }}
//             // filterOptions={(options, params) => {
//             //   const filtered = filter(options, params);

//             //   if (params.inputValue !== '') {
//             //     filtered.push({
//             //       inputValue: params.inputValue,
//             //       title: `Add "${params.inputValue}"`,
//             //     });
//             //   }

//             //   return filtered;
//             // }}
//             id="free-solo-dialog-demo"
//             options={'Bot'}
//             getOptionLabel={(option) => {
//               // e.g value selected with enter, right from the input
//               if (typeof option === 'string') {
//                 return option;
//               }
//               if (option.inputValue) {
//                 return option.inputValue;
//               }
//               return option.title;
//             }}
//             selectOnFocus
//             clearOnBlur
//             handleHomeEndKeys
//             renderOption={(props, option) => <li {...props}>{option.title}</li>}
//             sx={{ width: 300 }}
//             freeSolo
//             renderInput={(params) => <TextField {...params} label="Free solo dialog" />}
//           />
//           <Dialog open={this.state.open} onClose={handleClose}>
//             <form onSubmit={handleSubmit}>
//               <DialogTitle>Add a new film</DialogTitle>
//               <DialogContent>
//                 <DialogContentText>
//                   Did you miss any film in our list? Please, add it!
//                 </DialogContentText>
//                 <TextField
//                   autoFocus
//                   margin="dense"
//                   id="name"
//                   value={dialogValue.title}
//                   onChange={(event) =>
//                     setDialogValue({
//                       ...dialogValue,
//                       title: event.target.value,
//                     })
//                   }
//                   label="title"
//                   type="text"
//                   variant="standard"
//                 />
//                 <TextField
//                   margin="dense"
//                   id="name"
//                   value={dialogValue.year}
//                   onChange={(event) =>
//                     setDialogValue({
//                       ...dialogValue,
//                       year: event.target.value,
//                     })
//                   }
//                   label="year"
//                   type="number"
//                   variant="standard"
//                 />
//               </DialogContent>
//               <DialogActions>
//                 <Button onClick={handleClose}>Cancel</Button>
//                 <Button type="submit">Add</Button>
//               </DialogActions>
//             </form>
//           </Dialog> */}

//           {/* <input
//             type="text"
//             id="recipe_title"
//             name="recipe_title"
//             placeholder='Recipe Title'
//             value={this.state.val_recipe_title}
//             onChange={this.handleChange}
//             required
//             />
//           <input
//             type="text"
//             id="recipe_desc"
//             name="recipe_desc"
//             placeholder='Description'
//             value={this.state.val_recipe_desc}
//             onChange={this.handleChange}
//             required
//             />
//           <input
//             type="text"
//             id="ingredients"
//             name="ingredients"
//             placeholder='Ingredients'
//             value={this.state.val_ingredients}
//             onChange={this.handleChange}
//             required
//             />
//           <input
//             type="text"
//             id="prep_time"
//             name="prep_time"
//             placeholder='Prep Time (in minutes)'
//             value={this.state.val_prep_time}
//             onChange={this.handleChange}
//             required
//             />
//           <textarea
//             id="steps"
//             type='text'
//             name='steps'
//             placeholder='Steps'
//             value={this.state.val_steps}
//             onChange={this.handleChange}
//           /> */}
//           <input
//             id='submitBtn'
//             type="submit"
//             value="Submit"
//             />
//         </form>
//       </div>
//     );  
//   }
// }

const top100Films = [
  { title: 'The Shawshank Redemption', year: 1994 },
  { title: 'The Godfather', year: 1972 },
  { title: 'The Godfather: Part II', year: 1974 },
  { title: 'The Dark Knight', year: 2008 },
  { title: '12 Angry Men', year: 1957 },
  { title: "Schindler's List", year: 1993 },
  { title: 'Pulp Fiction', year: 1994 },
  {
    title: 'The Lord of the Rings: The Return of the King',
    year: 2003,
  },
  { title: 'The Good, the Bad and the Ugly', year: 1966 },
  { title: 'Fight Club', year: 1999 },
  {
    title: 'The Lord of the Rings: The Fellowship of the Ring',
    year: 2001,
  },
  {
    title: 'Star Wars: Episode V - The Empire Strikes Back',
    year: 1980,
  },
  { title: 'Forrest Gump', year: 1994 },
  { title: 'Inception', year: 2010 },
  {
    title: 'The Lord of the Rings: The Two Towers',
    year: 2002,
  },
  { title: "One Flew Over the Cuckoo's Nest", year: 1975 },
  { title: 'Goodfellas', year: 1990 },
  { title: 'The Matrix', year: 1999 },
  { title: 'Seven Samurai', year: 1954 },
  {
    title: 'Star Wars: Episode IV - A New Hope',
    year: 1977,
  },
  { title: 'City of God', year: 2002 },
  { title: 'Se7en', year: 1995 },
  { title: 'The Silence of the Lambs', year: 1991 },
  { title: "It's a Wonderful Life", year: 1946 },
  { title: 'Life Is Beautiful', year: 1997 },
  { title: 'The Usual Suspects', year: 1995 },
  { title: 'Léon: The Professional', year: 1994 },
  { title: 'Spirited Away', year: 2001 },
  { title: 'Saving Private Ryan', year: 1998 },
  { title: 'Once Upon a Time in the West', year: 1968 },
  { title: 'American History X', year: 1998 },
  { title: 'Interstellar', year: 2014 },
  { title: 'Casablanca', year: 1942 },
  { title: 'City Lights', year: 1931 },
  { title: 'Psycho', year: 1960 },
  { title: 'The Green Mile', year: 1999 },
  { title: 'The Intouchables', year: 2011 },
  { title: 'Modern Times', year: 1936 },
  { title: 'Raiders of the Lost Ark', year: 1981 },
  { title: 'Rear Window', year: 1954 },
  { title: 'The Pianist', year: 2002 },
  { title: 'The Departed', year: 2006 },
  { title: 'Terminator 2: Judgment Day', year: 1991 },
  { title: 'Back to the Future', year: 1985 },
  { title: 'Whiplash', year: 2014 },
  { title: 'Gladiator', year: 2000 },
  { title: 'Memento', year: 2000 },
  { title: 'The Prestige', year: 2006 },
  { title: 'The Lion King', year: 1994 },
  { title: 'Apocalypse Now', year: 1979 },
  { title: 'Alien', year: 1979 },
  { title: 'Sunset Boulevard', year: 1950 },
  {
    title: 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb',
    year: 1964,
  },
  { title: 'The Great Dictator', year: 1940 },
  { title: 'Cinema Paradiso', year: 1988 },
  { title: 'The Lives of Others', year: 2006 },
  { title: 'Grave of the Fireflies', year: 1988 },
  { title: 'Paths of Glory', year: 1957 },
  { title: 'Django Unchained', year: 2012 },
  { title: 'The Shining', year: 1980 },
  { title: 'WALL·E', year: 2008 },
  { title: 'American Beauty', year: 1999 },
  { title: 'The Dark Knight Rises', year: 2012 },
  { title: 'Princess Mononoke', year: 1997 },
  { title: 'Aliens', year: 1986 },
  { title: 'Oldboy', year: 2003 },
  { title: 'Once Upon a Time in America', year: 1984 },
  { title: 'Witness for the Prosecution', year: 1957 },
  { title: 'Das Boot', year: 1981 },
  { title: 'Citizen Kane', year: 1941 },
  { title: 'North by Northwest', year: 1959 },
  { title: 'Vertigo', year: 1958 },
  {
    title: 'Star Wars: Episode VI - Return of the Jedi',
    year: 1983,
  },
  { title: 'Reservoir Dogs', year: 1992 },
  { title: 'Braveheart', year: 1995 },
  { title: 'M', year: 1931 },
  { title: 'Requiem for a Dream', year: 2000 },
  { title: 'Amélie', year: 2001 },
  { title: 'A Clockwork Orange', year: 1971 },
  { title: 'Like Stars on Earth', year: 2007 },
  { title: 'Taxi Driver', year: 1976 },
  { title: 'Lawrence of Arabia', year: 1962 },
  { title: 'Double Indemnity', year: 1944 },
  {
    title: 'Eternal Sunshine of the Spotless Mind',
    year: 2004,
  },
  { title: 'Amadeus', year: 1984 },
  { title: 'To Kill a Mockingbird', year: 1962 },
  { title: 'Toy Story 3', year: 2010 },
  { title: 'Logan', year: 2017 },
  { title: 'Full Metal Jacket', year: 1987 },
  { title: 'Dangal', year: 2016 },
  { title: 'The Sting', year: 1973 },
  { title: '2001: A Space Odyssey', year: 1968 },
  { title: "Singin' in the Rain", year: 1952 },
  { title: 'Toy Story', year: 1995 },
  { title: 'Bicycle Thieves', year: 1948 },
  { title: 'The Kid', year: 1921 },
  { title: 'Inglourious Basterds', year: 2009 },
  { title: 'Snatch', year: 2000 },
  { title: '3 Idiots', year: 2009 },
  { title: 'Monty Python and the Holy Grail', year: 1975 },
];

// export default InputForm;