import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Dependencies
with open("requirements.txt", 'r') as reqs:
  dependencies = reqs.readlines()
dependencies = [x.strip() for x in dependencies]

# This call to setup() does all the work
setup(
    name="food-fighters",
    version="0.3.13",
    description="API Endpoints for Food Fighters project",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Food Fighters",
    license="MIT",
    packages=["backend"],
    include_package_data=True,
    install_requires=dependencies,
    entry_points={
        "console_scripts": [
            "foodfighters=backend.app:main",
        ]
    },
)
