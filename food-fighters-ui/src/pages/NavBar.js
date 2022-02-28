import './NavBar.css';
import ffLogo from '../assets/logos/ff-logo.png'

import React, { useState } from 'react';
import {Link} from 'react-router-dom';

export default function NavBar() {
  const [active, setActive] = useState('Home');

  return (
    <div className='navBar'>
      <Link to='/'>
        <button className='btn' id='ffLogoBtn'>
          <img 
              id='ffLogo' src={ffLogo} alt='FF Logo' 
              onClick={() => setActive('Home')}
          />
        </button>
      </Link>

      <div id='navPaths'>
        <Link to='/'>
          <button 
              className={`btn navBtn ${active === 'Home' ? 'activeBtn' : ''}`}
            onClick={() => setActive('Home')}
          >Home</button>
        </Link>

        <Link to='/Recipe'>
          <button 
              className={`btn navBtn ${active === 'Recipe' ? 'activeBtn' : ''}`}
              onClick={() => setActive('Recipe')}
          >Recipes</button>
        </Link>

        <Link to='/AboutUs'>
          <button 
              className={`btn navBtn ${active === 'About Us' ? 'activeBtn' : ''}`}
              onClick={() => setActive('About Us')}
          >About Us</button>
        </Link>

        <Link to='/Contact'>
          <button 
              className={`btn navBtn ${active === 'Contact' ? 'activeBtn' : ''}`}
              onClick={() => setActive('Contact')}
          >Contact</button>
        </Link>

        <Link to='/Account'>
          <button 
              className={`btn navBtn ${active === 'Account' ? 'activeBtn' : ''}`}
              onClick={() => setActive('Account')}
          >Account</button>
        </Link>
      </div>
    </div>
  );
};
