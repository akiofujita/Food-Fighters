import './App.css';
import NavBar from './pages/NavBar';
import Footer from './pages/Footer';
import HomePage from './pages/home/HomePage'
import RecipePage from './pages/recipe/RecipePage'
import ListPage from './pages/list/ListPage'
import AboutPage from './pages/about/AboutPage'

import {
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom';

export default function App() {
  return (
    <Router>
    <div className='App'>
      <link rel='preconnect' href='https://fonts.googleapis.com'/>
      <link rel='preconnect' href='https://fonts.gstatic.com' crossorigin/>
      <link href='https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap' rel="stylesheet" />
        
      <NavBar />

      <Routes>
        <Route exact path='/'   element={<HomePage/>} />
        <Route path='/Add'      element={<RecipePage/>} />
        <Route path='/List'     element={<ListPage/>} />
        <Route path='/AboutUs'  element={<AboutPage/>} />
      </Routes>
      
      <div className="container"></div>

      <Footer/>
      </div>
    </Router>
  );
};
