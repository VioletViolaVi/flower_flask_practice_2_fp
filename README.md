# Flower Flask Practice 2

A site for all your petal-related needs.

### Installation & development

- `pipenv install --dev`: install all required packages
- `pipenv run dev`: run the development server

### Testing

- `pipenv run test`: run all tests
- `pipenv run coverage`: generate a coverage report

## What actually worked for me tho...

### Testing

- `python -m pipenv install pytest pytest-cov`: installing pytest & pytest-cov
- `python -m pipenv install --dev pytest pytest-cov`: installing pytest & pytest-cov with **_`--dev`_**
- `python -m coverage run -m pytest`: running coverage
- `pipenv run coverage`: generate a coverage report **_(must have correct content in respective section of the Pipfile\*... ...\*see [Pipfile](./Pipfile))_**

### Flask, Werkzeug, Flask Cors

- `python -m pip install flask-cors werkzeug`: installing flask-cors & werkzeug
- `python -m pipenv install flask-cors werkzeug`: installing flask-cors & werkzeug
- `python -m pipenv install flask`: installing flask

### Running project

- `python app.py` **_(or whatever the main .py file is called)_**: results in Debug mode: on
- `python -m flask run`: results in Debug mode: off
  - unless you put `dev = "bash -c \"export FLASK_DEBUG=true && flask run\""` in a [Pipfile](./Pipfile) under **_scripts_**
- `python -m pipenv run dev`: results in Debug mode: off
  - unless you put `dev = "bash -c \"export FLASK_DEBUG=true && flask run\""` in a [Pipfile](./Pipfile) under **_scripts_**
