# CCE Search Prototype

An unofficial, experimental interface to search records digitized by NYPL's
[Catalog of Copyright Entries project](https://github.com/NYPL/catalog_of_copyright_entries_project).

Forked from Sean Redmond's [original protype](https://github.com/seanredmond/cce-search-prototype).

## Setting up the virtual environment

Using a virtual environment is very important for ensuring that all work is done in a standardized Python environment. This is a quick and dirty guide to working with the virtual environment, for a more detailed guide, read [this](https://docs.python.org/3.7/tutorial/venv.html). 

*Note: these commands all assume your system refers to your Python 3 installation as `python3`. On your system it may be different. You should confirm this before you try these commands.*

### Creating a new virtual environment

You shouldn't have to do this. However, in case something happens and the venv needs to be rebuilt, run the command:

`python3 -m venv env`

This will create a virtual environment in the directory `env/`.

### Activating the virtual environment

**Always do this before doing any development work!**

After activation, your shell prompt should change to reflect the environment you are working in.

#### Mac/Linux

`source env/bin/activate`

#### Windows

`env\Scripts\activate.bat`

### Installing required packages

**Do this the first time you work on the project (after activating the venv).**

`pip install -r requirements.txt`

### Regenerating `requirements.txt`

**Do this whenever you install a new package for this package.**

`pip freeze > requirements.txt`

### Deactivating the virtual environment

**Always do this when you're finished working, otherwise your other Python work will screw up the project!**

#### Mac/Linux

`source env/bin/deactivate`

#### Windows

`env\Scripts\deactivate.bat`