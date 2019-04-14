# Porygon Indexer

[![Build Status](https://travis-ci.org/aHugues/porygon-indexer.svg?branch=master)](https://travis-ci.org/aHugues/porygon-indexer)
[![codecov](https://codecov.io/gh/aHugues/porygon-indexer/branch/master/graph/badge.svg)](https://codecov.io/gh/aHugues/porygon-indexer)

Indexer for the Porygon project deployed  in a **Docker** container setup with unit testing 
with coverage testing and a production build using **gunicorn**.

## Getting started

Install Docker and run:

```shell
docker-compose up
```

Otherwise, you can run as standalone (using Python 3):

```shell
pip install -r requirements.txt
python app.py
```

The server can now be reached at http://localhost:5000.

## Development build

You can use Docker to build a development image:

```shell
docker-compose build
docker run -p 5000:5000 porygon-indexer-dev:1.0.0
```

## Tests

You can run the tests as standalone using **pytest** (only for unit tests)

```shell
pip install pytest pytest-cov pytest-flask
python -m pytest --cov=web/ --ignore=tests/integration tests
```

You can also run the tests using Docker (can include integration tests)

```shell
docker-compose -f test.yml -p ci build
docker-compose -f test.yml -p ci run test python -m pytest --cov=web/ tests
docker stop ci_web_1
```

This is integrated to TravisCi and the coverage results are reported to codecov.io.

## Production

You can run the application in production mode as standalone using:

```shell
pip install gunicorn
gunicorn wsgi:app -b 127.0.0.1:5000
```

The application can be reached like but only from locahost. You can now use a 
reverse proxy like nginx to correctly make it publicly accessible.

Replace `127.0.0.1:5000` by `0.0.0.0:5000` to make it publicly accessible using
port 5000.

You can run a production build with gunicorn using 

```shell
docker-compose -f production.yml build
```

The image can now be ran using 

```shell
docker run -p 127.0.0.1:5000:5000 porygon-indexer:1.0.0
```

Here again, you can replace `127.0.0.1:5000:5000` by `5000:5000` to make it 
publicly accessible from everywhere.

You can also use the `-d` flag to run it as a deamon. 
