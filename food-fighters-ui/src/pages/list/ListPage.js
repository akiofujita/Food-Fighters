import './ListPage.css';
import '../../App.css';
import RecipeCardList from './RecipeCardList';

export default function ListPage() {
  return (
    <div className='listPage'>
      <h2>Your Recipes</h2>
      <RecipeCardList />
    </div>
  );
};
