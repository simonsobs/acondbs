[![PyPI version](https://badge.fury.io/py/acondbs.svg)](https://badge.fury.io/py/acondbs) [![Test Status](https://github.com/simonsobs/acondbs/workflows/Test/badge.svg)](https://github.com/simonsobs/acondbs/actions?query=workflow%3ATest) [![codecov](https://codecov.io/gh/simonsobs/acondbs/branch/master/graph/badge.svg)](https://codecov.io/gh/simonsobs/acondbs)

# Acondbs

A GraphQL server for product DB

## How to check out and run (for developers)

### Prepare environment

Create a virtual environment

```bash
python -m venv venv
```

Enter the virtual environment

```bash
source venv/bin/activate
```

Upgrade pip (optional)

```bash
pip install --upgrade pip
```

### Check out

Clone the repository from GitHub

```bash
git clone git@github.com:simonsobs/acondbs.git
```

Install from the clone in the [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs).

```bash
pip install -e acondbs/[tests]
```

### Configure

Create an instance folder of Flask, where the config file and the SQLite DB file are stored. Check out an example instance folder from GitHub

```bash
git clone git@github.com:TaiSakuma/acondbs-instance-example.git instance
```

Set environmental variables

```bash
export FLASK_APP="acondbs:create_app('$PWD/instance/config.py')"
export FLASK_ENV=development
```

### Initialize database

```bash
flask init-db
```

An SQLite DB file has been created in the instance folder (`instance/product.sqlite3`). Tables were defined (The tables were empty. Only fields were defined. No data were inserted in the tables).

### Load sample data to DB (optional)

(Optional) Load sample data to the dababase.

```bash
flask import-csv acondbs/tests/sample/csv/
```

### Run

Run with the Flask built-in server for the development. (Deployment options for proudction are descriped in the [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/deploying/).)

```bash
flask run
```

The above command starts the built-in server that only allows accress from localhost. It starts the server at the default TCP port, usually `5000`.

To allow the access from outside, use `--host=0.0.0.0` option. The TCP port can be specified by `--port` option. For example:

```bash
flask run --host=0.0.0.0 --port=5000
```

#### Access to the server with cURL

Now, you can send GraphQL requests to the server, for example, as follows.

```bash
curl -d "query={allMaps { edges { node { name mapper } } }}" localhost:5000/graphql
```

#### Access to the server with a web browser

If you access to the server with a web browser, it will show a graphical user interface *GraphiQL*: <http://localhost:5000/graphql>

### Unit test

Move to the repository

```bash
cd acondbs
```

Run the unit tests

```bash
pytest
```

Run the unit tests with coverage

```bash
pytest --cov
```

Generate the coverage report

```bash
coverage html
```

The report can be found at `coverage_html_report/index.html`.
