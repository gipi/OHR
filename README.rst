Open Hardware Repository
==============================

Repository of Open Hardware projects

![travis build status](https://travis-ci.org/gipi/OHR.svg)

LICENSE: BSD

Getting Started
---------------

Exists a configuration script to be sourced:

    $ source bin/activate

that enable the ``m`` command as alias to ``manage.py`` script.

It's also possible to use the ``docker-compose`` application (installable by ``pip``)::

    $ docker-compose -f dev.yml build
    $ docker-compose -f dev.yml up -d
    $ docker-compose logs
    $ docker-compose -f dev.yml run --rm django python manage.py

Settings
------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.org/en/latest/settings.html

Basic Commands
--------------

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html
    $ coverage report
    Name                          Stmts   Miss  Cover
    -------------------------------------------------
    OWR/__init__                      2      0   100%
    OWR/contrib/__init__              0      0   100%
    OWR/contrib/sites/__init__        0      0   100%
    OWR/oh/__init__                   0      0   100%
    OWR/oh/factory                    8      0   100%
    OWR/oh/models                    48     13    73%
    OWR/oh/tests                     60      0   100%
    OWR/oh/urls                       4      0   100%
    OWR/oh/views                     26      0   100%
    OWR/users/__init__                0      0   100%
    OWR/users/admin                  24      0   100%
    OWR/users/factory                 9      0   100%
    OWR/users/models                 13      0   100%
    OWR/users/tests/__init__          0      0   100%
    OWR/users/tests/test_admin       17      0   100%
    OWR/users/tests/test_models       8      0   100%
    OWR/users/tests/test_views       25      0   100%
    OWR/users/urls                    4      0   100%
    OWR/users/views                  24      0   100%
    -------------------------------------------------
    TOTAL                           272     13    95%

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.org/en/latest/live-reloading-and-sass-compilation.html







It's time to write the code!!!


Running end to end integration tests
------------------------------------

N.B. The integration tests will not run on Windows.

To install the test runner::

  $ pip install hitch

To run the tests, enter the OWR/tests directory and run the following commands::

  $ hitch init

Then run the stub test::

  $ hitch test stub.test

This will download and compile python, postgres and redis and install all python requirements so the first time it runs it may take a while.

Subsequent test runs will be much quicker.

The testing framework runs Django, Celery (if enabled), Postgres, HitchSMTP (a mock SMTP server), Firefox/Selenium and Redis.
