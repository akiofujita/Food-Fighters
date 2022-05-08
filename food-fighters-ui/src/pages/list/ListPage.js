import RecipeCardList from './RecipeCardList';
import './ListPage.css';
import '../../App.css';

// Page that displays list of custom recipes
export default function ListPage() {
  return (
    <div className='listPage'>
      <h2>My Saved Recipes</h2>
      <RecipeCardList />
    </div>
  );
};
