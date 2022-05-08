import React, {useState} from 'react';
import TextField from '@mui/material/TextField';
import AddIcon from '@mui/icons-material/Add';
import RemoveIcon from '@mui/icons-material/Remove';
import IconButton from '@mui/material/IconButton';
import {ThemeProvider} from '@mui/material/styles';
import {theme} from '../../ColorTheme';
import './StepForm.css';

export default function StepForm() {
  const [inputList, setInputList] = useState(['']);

  // handle input change
  const handleInputChange = (e, index) => {
    const list = [...inputList];
    list[index] = e.target.value;
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
    setInputList([...inputList, '']);
  };

  return (
    <div className='stepsForm'>
      <h3>Step Details</h3>
      <div className='stepsList'>
        {inputList.map((step, i) => {
          return (
            <div className='stepsItem' key={i}>
              <div className='stepsField'>
                <h5 className='stepsNum'>{'Step ' + (i + 1).toString()}</h5>
                <TextField
                  required
                  name='steps'
                  label={'Step ' + (i + 1).toString()}
                  value={step ? step : ''}
                  onChange={e => handleInputChange(e, i)}
                  id='steps'
                  sx={{ width: '90%' }}
                />
              </div>
              <div className='removeBtn2'>
                {inputList.length !== 1 &&
                  <ThemeProvider theme={theme}>
                    <IconButton
                      color='secondary'
                      onClick={() => handleRemoveClick(i)}
                      aria-label='Remove Ingredient'
                    >
                      <RemoveIcon />
                    </IconButton>
                  </ThemeProvider>
                }
              </div>
              <div className='addBtn2'>
                {inputList.length - 1 === i &&
                  <ThemeProvider theme={theme}>
                    <IconButton
                      color='primary'
                      onClick={handleAddClick}
                      aria-label='Add Ingredient'>
                      <AddIcon />
                    </IconButton>
                  </ThemeProvider>
                }
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
