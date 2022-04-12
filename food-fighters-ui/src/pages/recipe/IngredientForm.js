import React, {useState, useEffect} from 'react';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import './IngredientForm.css'

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
  },
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
    // alert(e.target.name);
    // // alert(JSON.stringify(e.target));
    // alert(value);
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
    <div className='ing-gen'>
      <h3>Ingredient Details</h3>
      {inputList.map((values, i) => {
        return (
          <div className='ing-form'>
            <TextField
              required
              name="ing_name"
              label="Name"
              value={values.ing_name}
              onChange={e => handleInputChange(e, i)}
              id="ing_name"
              sx={{ m: 1, width: '35ch' }}
            />
            <TextField
              required
              name='ing_quant'
              label="Quantity"
              value={values.ing_quant}
              onChange={e => handleInputChange(e, i)}
              id="ing_quant"
              sx={{ m: 1, width: '12ch' }}
            />
            <TextField
              required
              select
              name='ing_units'
              label="Units"
              value={values.ing_units}
              onChange={e => handleInputChange(e, i)}
              id="ing_units"
              sx={{ m: 1, width: '20ch' }}
            >
              {units.map((option) => (
                <MenuItem key={option.key} value={option.key}>
                  {option.label}
                </MenuItem>
              ))}
            </TextField>
            <div className="btn-box">
              {inputList.length !== 1 && <button
                className="mr10"
                onClick={() => handleRemoveClick(i)}>Remove</button>}
              {inputList.length - 1 === i && <button onClick={handleAddClick}>Add</button>}
            </div>
          </div>
        );
      })}
      <div style={{ marginTop: 20 }}>{JSON.stringify(inputList)}</div>
    </div>
  );
}
