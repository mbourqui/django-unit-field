[![Python](https://img.shields.io/badge/Python-3.4,3.5,3.6-blue.svg?style=flat-square)](/)
[![Django](https://img.shields.io/badge/Django-1.8,1.9,1.10,1.11-blue.svg?style=flat-square)](/)
[![License](https://img.shields.io/badge/License-UNLICENSE-blue.svg?style=flat-square)](/UNLICENSE)
[![PyPI](https://img.shields.io/pypi/v/django_unitfield.svg?style=flat-square)](https://pypi.python.org/pypi/django-unitfield)
[![Build Status](https://travis-ci.org/mbourqui/django-unitfield.svg?branch=master)](https://travis-ci.org/mbourqui/django-unitfield)
[![Coverage Status](https://coveralls.io/repos/github/mbourqui/django-unitfield/badge.svg?branch=master)](https://coveralls.io/github/mbourqui/django-unitfield?branch=master)


django-unit-field
=================

Django specialized model field inherited from FloatField with unit
conversion by custom widget

Installation
------------

You will need to add `unit_field` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        # ...
        'unit_field',
    )

Abstract
--------

django-unit-field provides a set of Fields for your model. Each field
will create three columns in the corresponding database that holds all
required informations. These classes are located in `unit_field.fields`:

    * LengthField (base unit: m=1)
    * SquareMeasureField (base unit: m²=1)
    * SolidMeasureField (base unit: m³=1)
    * MassField (base unit: g=1)
    * TimeField (base unit: s=1)
    * TemperatureField (base unit: K=1)
    * AmountOfSubstanceField (base unit: mol=1)
    * LuminousIntensityField (base unit: cd=1)

Enhance your models
-------------------

Example:

    from unit_field.fields import SolidMeasureField, TemperatureField

    class Engine(models.Model):
        cubic_capacity = SolidMeasureField(
            verbose_name=u'cubic capacity')
        operating_temperature = TemperatureField(
            verbose_name=u'operatiing temperature')

Enable client-side unit conversion
----------------------------------

If you want to use client-side unit conversion, you have to include the
static javascript file located in the `static` directory of the app:

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/{{jquery-version}}/jquery.min.js"></script>
    <script src="{{ STATIC_URL }}js/jquery.unitfield.js"></script>

If you want to exclude some fields from automatic conversion, you can
use the additional parameter `auto_convert`:

    class Engine(models.Model):
        ...
        operating_temperature = TemperatureField(auto_convert=False,
            verbose_name=u'operatiing temperature')

Declare custom units
--------------------

TODO: Describe how to inherit from class `UnitField`.
