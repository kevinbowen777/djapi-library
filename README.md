## djapi-library

Basic library website & API built with Django & Djano REST Framework (DRF)

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

---
## Features
 - Basic browseable API
 - Admin management of books

### Live Demo on Heroku:
 - [kbowen-djapi-library](https://kbowen-djapi-library.herokuapp.com/)
 - [kbowen-djapi-library API Endpoint](https://kbowen-djapi-library.herokuapp.com/api)
 - [kbowen-djapi-library API JSON](http://kbowen-djapi-library/api/?format=json)

### Docker Container Image:
 - N/A

---
![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/djapi-library/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/djapi-library/issues)
      to view currently open bug reports or open a new issue.
