import './InputForm.css';
import React from 'react';

class InputForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      val_recipe_name: "",
      val_ingredients: "",
      val_prep_time:   "",
      val_steps:       ""
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({
      val_recipe_name: event.target.val_recipe_name,
      val_ingredients: event.target.val_ingredients,
      val_prep_time:   event.target.val_prep_time,
      val_steps:       event.target.val_steps
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
            value={this.state.val_recipe_name}
            onChange={this.handleChange}
            required
            />
          <input
            type="text"
            id="ingredients"
            name="ingredients"
            placeholder='Ingredients'
            value={this.state.val_ingredients}
            onChange={this.handleChange}
            required
            />
          <input
            type="text"
            id="prep_time"
            name="prep_time"
            placeholder='Prep Time'
            value={this.state.val_prep_time}
            onChange={this.handleChange}
            required
            />
          <textarea
            id="steps"
            type='text'
            name='steps'
            placeholder='Steps'
            value={this.state.val_steps}
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