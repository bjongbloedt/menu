# menu

## running menu

There are a few ways to run menu, the easiest of which is docker

### Docker

In the api directory run

```sh
# Builds a new image based on the dockerfile
docker build . -t menu

# Starts a new instance of menu
docker run -d -p 5000:5000 menu
```

After running those commands, the api should be avaiable at `http://localhost:5000/healthz`

### Via apistar (from scratch)

Note that this way will not bootstrap data in sqlite

#### Prereqs

This project is based on python 3.6.  Please see this [link](https://docs.python.org/3/using/index.html) on information about installing python

This project uses [pipenv](https://github.com/kennethreitz/pipenv) to manage its deps via the Piplock file.  To install pipenv run either

1. `pip install pipenv` with python installed on the system
1. `brew install pipenv` for mac only

### Installing requirements

`pipenv install --dev`

### Running server

From the api directory

```sh
# start the virtual environment created by pipenv
pipenv shell

# start the api star server
apistar run
```

### Running tests

From the api directory

```sh
# start the virtual environment created by pipenv
pipenv shell

# run the tests
apistar test
```

## Project structure
```
api
    project/
      models.py -> Location of sqlalchemy models
      routes.py -> api routes setup
      schemas.py -> Schema for request and response from views
      settings.py -> Generic settings for application
      views.py -> Handlers for the routes
    tests/
app.py -> File that pulls together the various project elements into runnable api
Dockerfile
load_db.py -> script to boostrap data into database
Pipfile -> pipenv file for deps
Pipfile.lock -> pipenv file for deps
```

## Next steps

1. Add route for `patch`ing fields on items
1. Improve documentation on schemas, and routes
1. Split out schemas, views files into smaller chunks
1. Hook up to containerized db in docker-compose env
1. Get alembic rigged up for db migrations
1. Need to add cascading delete so that when a Restaurant is deleted, its child menus, and items are also deleted.  Otherwise database will fill up with data that doesn't need to be there.
