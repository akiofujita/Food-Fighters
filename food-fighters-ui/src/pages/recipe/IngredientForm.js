import './IngredientForm.css';
import React, {useState} from 'react';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import AddIcon from '@mui/icons-material/Add';
import RemoveIcon from '@mui/icons-material/Remove';
import IconButton from '@mui/material/IconButton';
import {ThemeProvider} from '@mui/material/styles';
import {theme} from './ColorTheme'

const units = [
  {
    value: 'met-0',
    label: 'grams',
  },
  {
    value: 'imp-0',
    label: 'tbsp',
  },
  {
    value: 'misc-0',
    label: 'pinch',
  }
];

export default function IngredientForm() {
  const [inputList, setInputList] = useState([{
    ing_name: "",
    ing_quant: "",
    ing_units: ""
  }]);

  // handle input change
  const handleInputChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...inputList];
    list[index][name] = value;
    setInputList(list);
  };
  
  // handle click event of the Remove button
  const handleRemoveClick = (index) => {
    const list = [...inputList];
    list.splice(index, 1);
    setInputList(list);
  };
  
  // handle click event of the Add button
  const handleAddClick = () => {
    setInputList([...inputList, {
      ing_name: '',
      ing_quant: '',
      ing_units: '',
    }]);
  };

  return (
    <div className="ingredientForm">
      <h3>Ingredient Details</h3>
      <div className="ingredientList">
        {inputList.map((values, i) => {
          return (
            <div className="ingredientItem">
              <div className="ingredientField">
                <TextField
                  required
                  name="ing_name"
                  label="Name"
                  value={values ? values.ing_name : ""}
                  onChange={e => handleInputChange(e, i)}
                  id="ing_name"
                  sx={{ width: '50%' }}
                />
                <TextField
                  required
                  name='ing_quant'
                  label="Quantity"
                  value={values ? values.ing_quant : ""}
                  onChange={e => handleInputChange(e, i)}
                  id="ing_quant"
                  sx={{ width: '23%' }}
                />
                <TextField
                  required
                  select
                  name='ing_units'
                  label="Units"
                  value={values ? values.ing_units : ""}
                  onChange={e => handleInputChange(e, i)}
                  id="ing_units"
                  sx={{ width: '23%' }}
                >
                  {units.map((option) => (
                    <MenuItem key={option.value} value={option.value}>
                      {option.label}
                    </MenuItem>
                  ))}
                </TextField>
              </div>
              <div className="removeBtn">
                {inputList.length !== 1 &&
                  <ThemeProvider theme={theme}>
                    <IconButton
                      color="secondary"
                      onClick={() => handleRemoveClick(i)}
                      aria-label="Remove Ingredient"
                    >
                      <RemoveIcon />
                    </IconButton>
                  </ThemeProvider>
                }
              </div>
              <div className="addBtn">
                {inputList.length - 1 === i &&
                  <ThemeProvider theme={theme}>
                    <IconButton
                      color="primary"
                      onClick={handleAddClick}
                      aria-label="Add Ingredient">
                      <AddIcon />
                    </IconButton>
                  </ThemeProvider>
                }
              </div>
            </div>
          );
        })}
      </div>
      {/* <div style={{ marginTop: 20 }}>{JSON.stringify(inputList)}</div> */}
    </div>
  );
}
