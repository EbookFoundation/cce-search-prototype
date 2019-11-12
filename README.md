# CCE Search Prototype

An unofficial, experimental interface to search records digitized by NYPL's
[Catalog of Copyright Entries project](https://github.com/NYPL/catalog_of_copyright_entries_project).

Forked from Sean Redmond's [original protype](https://github.com/seanredmond/cce-search-prototype).

## Required software

- Python 3.7
- Pipenv

## Using Pipenv

Using a virtual environment is very important for ensuring that all work is done in a standardized Python environment. In order to simplify using a virtual environment as well as to give us the ability to create deterministic builds, we use [Pipenv](https://realpython.com/pipenv-guide/).

### Installing Pipenv

#### Mac

`brew install pipenv`

*Note: Mac users can also install through Pip, but using Homebrew is recommended.*

#### Other systems

`pip install --user pipenv`

*Note: You may have versions of Pip installed for both Python 2 and 3. If so, your Python 3 Pip will be called pip3. Check if this is the case by running `pip --version` and `pip3 --version`.*

### First time package install

Run `pipenv install` in the project's main directory.

### Installing new packages

In the project directory, use `pipenv install` the same way you would use `pip install`. The package will be installed in the virtual environment, and the Pipfile will be updated.

For example, to install the package requests: `pipenv install requests`

To specify a specific package version: `pipenv install flask==0.12.1`

To install packages for development purposes (e.g. ones that aren't required to build and run the project, but are useful for working on it), you can use the --dev flag. For example, `pipenv install pytest --dev`. 

### Activating the virtual environment

To activate the virtual environment in your current shell, run `pipenv shell`. The virtual environment will be indicated by a change to your terminal prompt.

### "Locking" the virtual environment

To ensure a deterministic build and "lock" the versions of packages and their subdependencies, run `pipenv lock`. This will ensure Pipfile.lock is up to date. Do this when any changes are made for the production environment.

### Remove an unneeded package

To remove a package from the Pipfile and uninstall it from your virtual environment, use `pipenv uninstall`.

For example, to remove beautifulsoup: `pipenv uninstall beautifulsoup`

### Run a command in the virtual environment without activating it

`pipenv run [command_goes_here]`

### Closing the virtual environment

After you have activated the virtual environment, press `ctrl-d` to exit. Your terminal prompt should return to its original appearance.

**Always do this when you're finished working in the virtual environment, otherwise your other Python work will screw up the project!**

## Deploying the project locally

After activating the virtual environment, run the following command from within the root directory of the project:

`gunicorn -w=4 wsgi:app`

This will run the Flask application on a Gunicorn WSGI server. You can then go to [localhost:8000](localhost:8000) to use the application.

To close the application, end the process with `ctrl-c` in your terminal. 

**TODO:**

- Update Gunicorn config file to automatically specify number of worker processes
- Use nginx to keep Gunicorn behind proxy server, as seen [here](https://gunicorn.org/#deployment)