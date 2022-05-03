import './ListPage.css';
import '../../App.css';
import RecipeCardList from './RecipeCardList';

export default function ListPage() {
  return (
    <div className='listPage'>
      <h2>My Saved Recipes</h2>
      <RecipeCardList />
    </div>
  );
};
