.. _`changelog`:

=========
Changelog
=========

``djapi-library`` issues are filed on `GitHub <https://github.com/kevinbowen777/djapi-library/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

djapi-library 0.3.5 (2026-08-03)
================================

Improved documentation
----------------------

-  (`#553 <https://github.com/kevinbowen777/djapi-library/issues/553>`_): Add towncrier 25.8.0.


New features
------------

-  (`#578 <https://github.com/kevinbowen777/djapi-library/issues/578>`_): Upgrade to Django 6.0.8

djapi-library 0.3.4 (2026-07-31)
================================

Contributor-facing changes
--------------------------

- : Add Python 3.14 support.

-  (`#574 <https://github.com/kevinbowen777/djapi-library/issues/574>`_): Rename default branch to main.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#568 <https://github.com/kevinbowen777/djapi-library/issues/568>`_): Drop support for Python 3.11.


New features
------------

-  (`#537 <https://github.com/kevinbowen777/djapi-library/issues/537>`_): Upgrade Django to 6.0.7.

djapi-library 0.3.3 (2025-05-08)
================================

Contributor-facing changes
--------------------------

-  (`#483 <https://github.com/kevinbowen777/djapi-library/issues/483>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#478 <https://github.com/kevinbowen777/djapi-library/issues/478>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#477 <https://github.com/kevinbowen777/djapi-library/issues/477>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#422 <https://github.com/kevinbowen777/djapi-library/issues/422>`_): Upgrade Docker image to Python 3.13

-  (`#482 <https://github.com/kevinbowen777/djapi-library/issues/482>`_): Upgrade Django Rest Framework to 3.16.0.

-  (`#484 <https://github.com/kevinbowen777/djapi-library/issues/484>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#487 <https://github.com/kevinbowen777/djapi-library/issues/487>`_): Replace safety package with pip-audit.

djapi-library 0.3.2 (2025-01-24)
================================

Contributor-facing changes
--------------------------

-  (`#416 <https://github.com/kevinbowen777/djapi-library/issues/416>`_): Add support for Python 3.13

-  (`#460 <https://github.com/kevinbowen777/djapi-library/issues/460>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#451 <https://github.com/kevinbowen777/djapi-library/issues/451>`_): Upgrade Django to 5.1.4

djapi-library 0.3.0 (2023-12-25)
================================

Contributor-facing changes
--------------------------

-  (`#169 <https://github.com/kevinbowen777/djapi-library/issues/169>`_): Migrate to non-root Docker user & venv.

-  (`#173 <https://github.com/kevinbowen777/djapi-library/issues/173>`_): Update Python to 3.12.0.

-  (`#323 <https://github.com/kevinbowen777/djapi-library/issues/323>`_): Upgrade Poetry to 1.7.1.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#320 <https://github.com/kevinbowen777/djapi-library/issues/320>`_): Drop support for Python 3.9.


Improved documentation
----------------------

- : Update Sphinx theme to Furo


New features
------------

-  (`#331 <https://github.com/kevinbowen777/djapi-library/issues/331>`_): Upgrade to Django 5.0.

djapi-library 0.2.0 (2023-05-16)
================================

Contributor-facing changes
--------------------------

-  (`#206 <https://github.com/kevinbowen777/djapi-library/issues/206>`_): Install ruff. Drop flake8-* packages.

djapi-library 0.1.0 (2023-05-08)
================================

Contributor-facing changes
--------------------------

- : Add django-debug-toolbar.

- : Implement Swagger-UI API View

- : Migrate from pipenv to Poetry

- : Mirror to GitLab.

-  (`#166 <https://github.com/kevinbowen777/djapi-library/issues/166>`_): Migrate from SQLite to PostgreSQL

-  (`#178 <https://github.com/kevinbowen777/djapi-library/issues/178>`_): Add support for Python 3.12.

-  (`#185 <https://github.com/kevinbowen777/djapi-library/issues/185>`_): Re-write for compatibility with Poetry 1.4.1.

-  (`#189 <https://github.com/kevinbowen777/djapi-library/issues/189>`_): Upgrade PostgreSQL to 15.2

-  (`#207 <https://github.com/kevinbowen777/djapi-library/issues/207>`_): Upgrade Django to 4.2.1

-  (`#3 <https://github.com/kevinbowen777/djapi-library/issues/3>`_): Implement nox for testing


Improved documentation
----------------------

- : Add Sphinx for documentation

djapi-library 0.0.1 (2022-07-19)
================================

Contributor-facing changes
--------------------------

- : Add support for Python 3.10


New features
------------

- : Build Docker support for Heroku deployment.

- : Support Django 4.0.6


Miscellaneous internal changes
------------------------------

- : Initial commit
