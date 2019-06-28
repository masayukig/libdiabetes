========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-libdiabetes/badge/?style=flat
    :target: https://readthedocs.org/projects/python-libdiabetes
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/masayukig/python-libdiabetes.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/masayukig/python-libdiabetes

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/masayukig/python-libdiabetes?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/masayukig/python-libdiabetes

.. |requires| image:: https://requires.io/github/masayukig/python-libdiabetes/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/masayukig/python-libdiabetes/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/masayukig/python-libdiabetes/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/masayukig/python-libdiabetes

.. |codecov| image:: https://codecov.io/github/masayukig/python-libdiabetes/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/masayukig/python-libdiabetes

.. |version| image:: https://img.shields.io/pypi/v/libdiabetes.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/libdiabetes

.. |commits-since| image:: https://img.shields.io/github/commits-since/masayukig/python-libdiabetes/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/masayukig/python-libdiabetes/compare/v0.0.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/libdiabetes.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/libdiabetes

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/libdiabetes.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/libdiabetes

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/libdiabetes.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/libdiabetes


.. end-badges

.. warning::

   This project is under heavy primary phase which means this project has not
   actual code yet.

Libraries for fighting against diabetes

* Free software: Apache Software License 2.0

What is this?
=============

Minimal Features
----------------

* Records blood glucose/sugar, HbA1c, blood pressure, ketone, etc. *easily*

Possible Features
-----------------

* graph
* export data
* Connect with Google Fit
* Docker image
* interact with Git (not sure the exact feature
* Dictionary for amounts of carbohydrate
* Recognize Good/Bad foods from images w/ ML
* playing with pandas?
* Coordinate with voice assistant?
* Predict BS level from carbohydrate consumption (is this possible?)


Installation
============

::

    pip install libdiabetes

Documentation
=============

https://python-libdiabetes.readthedocs.io/

Development
===========

To run the all tests run::

    tox
