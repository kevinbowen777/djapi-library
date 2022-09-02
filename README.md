## djapi-library

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/djapi-library.svg)](https://github.com/kevinbowen777/djapi-library/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

 - Basic library website & API built with Django & Djano REST Framework (DRF)

---
## Features
 - Browseable Web API
 - SwaggerUI & ReDoc API documentation
 - User registration with email verification & social(GitHub) login
 - Bootstrap4 & crispy-forms decorations
 - Customizable user profiles with bio, profile picture & country flags
 - Nox testing sessions (black, linting, pytest, coverage, Sphinx doc generation)

---
### Installation
 - `git clone https://github.com/kevinbowen777/djapi-library.git`
 - `cd djapi-library`
 - `poetry install`
 - `poetry shell`
 - `python manage.py runserver`
 - `python manage.py migrate`
 - `python manage.py createsuperuser`
 - Open browser to http://127.0.0.1:8000
 
---
### URLs
 - Log In endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/login/
 - Log Out endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/
 - Password reset:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset
 - Password reset confirmation:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset/confirm
 - User registration endpoint:
    http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/
 - User list:
    http://127.0.0.1:8000/api/v1/users/
 - User detail:
    http://127.0.0.1:8000/api/v1/users/1/
 - API schema download:
    http://127.0.0.1:8000/api/schema/
 - Redoc API browser:
    http://127.0.0.1:8000/api/schema/redoc/
 - Swagger-UI:
    http://127.0.0.1:8000/api/schema/swagger-ui/

---

### Live Demo on Heroku:
 - [kbowen-djapi-library](https://kbowen-djapi-library.herokuapp.com/)
 - [kbowen-djapi-library API Endpoint](https://kbowen-djapi-library.herokuapp.com/api)
 - [kbowen-djapi-library API JSON](http://kbowen-djapi-library/api/?format=json)

---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/djapi-library/issues)
      to view currently open bug reports or open a new issue.
