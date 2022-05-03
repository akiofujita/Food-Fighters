import './AboutPage.css';
import '../../App.css';

export default function AboutPage() {
  return (
    <div className='aboutPage'>
      <div id='aboutHeader'>
        <h1>About Food Fighters!</h1>
      </div>
      <div id='aboutBody'>
        <p>
        Cooking is a constant battle between brainstorming what to cook and what ingredients you happen to have in the fridge/pantry at the time.
        Everything we buy at the grocery store vary in portions, and it’s easy to be left with an excess of ingredients.
        Particularly for busy college students, preparing ingredients and cooking them in a timely manner is also a large concern.
        We hope to create something that will lessen this burden so that people can quickly figure out what to make in a timely manner and eventually shop efficiently as well.
        </p>
        <ul>
          <li><a href="https://www.npmjs.com/package/food-fighters-ui">Open Source Frontend</a></li>
          <li><a href="https://pypi.org/project/food-fighters/0.3.13/">Open Source Backend</a></li>
        </ul>
      </div>
    </div>
  );
};
