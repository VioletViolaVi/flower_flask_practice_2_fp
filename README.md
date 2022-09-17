# Flower Flask Practice 2

A site for all your petal-related needs.

### Installation & development

- `pipenv install --dev`: install all required packages
- `pipenv run dev`: run the development server

### Testing

- `pipenv run test`: run all tests
- `pipenv run coverage`: generate a coverage report

# What actually worked for me tho...

### Running project

- `python app.py` **_(or whatever the main .py file is called)_**: results in Debug mode: on
- `python -m flask run` **_OR_** `python -m pipenv run dev`: results in Debug mode: off
  - unless you put `dev = "bash -c \"export FLASK_DEBUG=true && flask run\""` in a [Pipfile](./Pipfile) under **_\[scripts\]_**

### Flask, Werkzeug, Flask Cors

- `python -m pip install flask flask-cors werkzeug`: installing flask, flask-cors & werkzeug
- `python -m pipenv install flask flask-cors werkzeug`: installing flask, flask-cors & werkzeug

### Testing

- `python -m pipenv run test`: runs tests
- `python -m pipenv run coverage`: runs coverage

- `python -m pipenv install --dev pytest pytest-cov`: installs pytest & pytest-cov with **_`--dev`_**
- `python -m pipenv install pytest pytest-cov`: installs pytest & pytest-cov **_NO --DEV!!!_**
- `python -m coverage run -m pytest`: runs coverage
- `python -m pipenv run coverage`: generates coverage report
  - **_(must have correct content in respective section of the Pipfile\*... ...\*see [Pipfile](./Pipfile))_**
