import React from "react";
import TextField from '@mui/material/TextField';

const IngredientList = props => {
  return props.ingDetails.map((val, idx) => {
    let ing_name = `ing_name-${idx}`,
      ing_quant = `ing_quant-${idx}`,
      ing_units = `ing_units-${idx}`
    alert(props.ingDetails);
    return (
      <div className="form-row" key={val.index}>
        <div className="col">
          <TextField
            required
            label="Name"
            sx={{ m: 1, width: '30ch' }}
            data-id={idx}
            id={ing_name}
          />
          <TextField
            required
            label="Quantity"
            sx={{ m: 1, width: '30ch' }}
            data-id={idx}
            id={ing_quant}
          />
        </div>
        <div className="col">
          <label>Units</label>
          <select className="form-control" name="units" id={ing_units} data-id={idx}>
            <option>g</option>
            <option>tbsp</option>
            <option>pinch</option>
          </select>
        </div>
        <div className="col p-4">
          {idx === 0 ? (
            <button
              onClick={() => props.add()}
              type="button"
              className="btn btn-primary text-center"
            >
              <i className="fa fa-plus-circle" aria-hidden="true" />
            </button>
          ) : (
            <button
              className="btn btn-danger"
              onClick={() => props.delete(val)}
            >
              <i className="fa fa-minus" aria-hidden="true" />
            </button>
          )}
        </div>
      </div>
    );
  });
};
export default IngredientList;
