Usage
=====

.. _installation:

Installation
------------

To use Food-Fighters, first install the API endpoints using pip:

.. code-block:: console

   (.venv) $ pip install food-fighters==0.3.13

Then install the UI using npm:

.. code-block:: console

   (.venv) $ npm i food-fighters-ui

Obtaining recipes
-----------------

Food Fighters will be using an open source recipe scraper to load in recipe data, which is then kept and refreshed in a database server. The documentation can be found at <https://pypi.org/project/recipe-scrapers/>.

To properly use the scraper, users will need to import the dump file into MySQL Workbench and start a connection. More documentation on MySQL setup can be found at <https://dev.mysql.com/doc/workbench/en/wb-getting-started-tutorial-create-connection.html>. 

The example database has 5 manually entered recipes to query from, and available scripts to query this information is within the scripts file in the data folder.

The scraper takes both allrecipe.com URLs and .csv files containing allrecipe.com URLs. An example .csv file is available in toget.csv.

To run with the .csv file:

.. code-block:: console
   
   (.venv) $ python3 backend/data/scraper.py backend/data/toget.csv

To run with a url:

.. code-block:: console

   (.venv) $ python3 backend/data/scraper.py https://www.allrecipes.com/recipe/228641/chef-johns-popovers/



