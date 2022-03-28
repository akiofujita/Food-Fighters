Food Fighters
===================================

.. image:: https://img.shields.io/pypi/v/food-fighters.svg?
    :target: https://pypi.org/project/food-fighters/0.3.13/
    :alt: Version
------

Project Description
----------

This web application will output recipes based on the ingredients the user inputs as well as overall cooking time of the recipes available, quickly recommending what to make for their meal. 
Users can also store their own recipes in the database, which would be included in future queries.

Approach
----------

This web application uses a Flask framework to connect our services together along with the React library for UI elements. 

.. image:: docs\source\FFschema.png
  :width: 400
  :alt: An image of the end-goal schema.

A database server run via mySQL will contain recipes for users to access, and will be populated using an open-source recipe scraper.

More about how to work on these components can be found at https://food-fighters.readthedocs.io/en/latest/


Development Roadmap
------------------------------------------

We are currently migrating from SQLite to mySQL as well as creating accounts with proper authentication and security measures. From there, we will be able to test recipe filtering and improve upon UI elements before releasing a beta. Users can currently input recipes via the webapp and save them within the database. Below you can find our version history.

- 0.1.0 – Commit 332b47d: This version features a primitive API for inputting recipes
- 0.1.x – CI/CD implementation
- 0.2.0 – Commit 946d854: This version has an API that queries for a result from database
- 0.2.1 – Commit 2b5163c: Added 3 test recipes and polished out the database structure/schema
- 0.3.0 – Commit 7296846: First commit merging/rebasing UI features
- 0.3.1-0.3.12 – Updating certain backend and frontend elements to prepare for midterm demo
- 0.3.13 – Commit (merge) 40fbf62: Syntax cleanup for app.py and updating dependencies


Inspiration
---------------------

The idea for this project came from wanting a more efficient way to brainstorm recipe ideas under a certain time limit and to search via ingredients to use produce more sustainably. SuperCook contains many of the features we hope to implement.

<https://www.supercook.com/>

    - Add/remove ingredients (for storage/search)
    - Queries websites with the ingredients to search for recipes
    - Allows users to keep track of favorite recipes and shopping list
