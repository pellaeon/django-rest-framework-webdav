djangorestframework-webdav
======================================

|build-status-image| |pypi-version|

Overview
--------

WebDAV renderers, views, serializers for Django REST Framework

Requirements
------------

-  Python (2.7, 3.3, 3.4, 3.5)
-  Django (1.8, 1.9, 1.10)
-  Django REST Framework (3.4, 3.5)

Installation
------------

Install using ``pip``\ …

.. code:: bash

    $ pip install djangorestframework-webdav

Example
-------

TODO: Write example.

Testing
-------

Install testing requirements.

.. code:: bash

    $ pip install -r requirements/requirements.txt

Run with runtests.

.. code:: bash

    $ ./runtests.py

You can also use the excellent `tox`_ testing tool to run the tests
against all supported versions of Python and Django. Install tox
globally, and then simply run:

.. code:: bash

    $ tox

Documentation
-------------

To build the documentation, you’ll need to install ``mkdocs``.

.. code:: bash

    $ pip install mkdocs

To preview the documentation:

.. code:: bash

    $ mkdocs serve
    Running at: http://127.0.0.1:8000/

To build the documentation:

.. code:: bash

    $ mkdocs build

.. _tox: http://tox.readthedocs.org/en/latest/

.. |build-status-image| image:: https://secure.travis-ci.org/pellaeon/django-rest-framework-webdav.svg?branch=master
   :target: http://travis-ci.org/pellaeon/django-rest-framework-webdav?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/djangorestframework-webdav.svg
   :target: https://pypi.python.org/pypi/djangorestframework-webdav
