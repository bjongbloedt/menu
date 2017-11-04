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