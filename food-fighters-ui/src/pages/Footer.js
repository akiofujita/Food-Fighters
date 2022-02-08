import './Footer.css'
import '../App.css'

import facebookLogo from '../assets/logos/facebook.png'
import instagramLogo from '../assets/logos/instagram.png'
import twitterLogo from '../assets/logos/twitter.png'
import youtubeLogo from '../assets/logos/youtube.png'

export default function Footer() {
  return (
    <div className='footer'>
      <div id='socials'>
        <a href='https://www.facebook.com/PurdueMIND/'>
          <img id='facebookLogo' className='socialLogo'
            src={facebookLogo} alt='Facebook Logo' />
        </a>

        <a href='https://www.instagram.com/purdue.mind/'>
          <img id='instagramLogo' className='socialLogo'
            src={instagramLogo} alt='Instagram Logo' />
        </a>

        <a href='https://twitter.com/purduemind?lang=en'>
          <img id='twitterLogo' className='socialLogo'
            src={twitterLogo} alt='Twitter Logo' />
        </a>

        <a href='https://www.youtube.com/channel/UC6Dv-UygUz6vUts8L8hGi8g/featured'>
          <img id='youtubeLogo' className='socialLogo'
            src={youtubeLogo} alt='YouTube Logo' />
        </a>
      </div>

      <h5 id='copyright'>CREATED AND MAINTAINED BY FOOD FIGHTERS | COPYRIGHT 2022 | ALL RIGHTS RESERVED</h5>
    </div>
  );
} 