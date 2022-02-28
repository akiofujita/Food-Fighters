import './InputForm.css';
import React from 'react';

class InputForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value_recipe_name: "",
      value_ingredients: "",
      value_steps: ""
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({
      value_recipe_name: event.target.value_recipe_name,
      value_ingredients: event.target.value_ingredients,
      value_steps: event.target.value_steps
    });
  }

  render() {
    return (
      <div className="inputForm">
        <form action="submitrecipe" method="post">
          <input
            type="text"
            id="recipe_name"
            name="recipe_name"
            placeholder='Recipe Name'
            value={this.state.value_recipe_name}
            onChange={this.handleChange}
            required
            />
          <input
            type="text"
            id="ingredients"
            name="ingredients"
            placeholder='Ingredients'
            value={this.state.value_ingredients}
            onChange={this.handleChange}
            required
            />
          <textarea
            id="steps"
            type='text'
            name='steps'
            placeholder='Steps'
            value={this.state.steps}
            onChange={this.handleChange}
          />
          <input
            id='submitBtn'
            type="submit"
            value="Submit"
            />
        </form>
      </div>
    );  
  }
}

export default InputForm;