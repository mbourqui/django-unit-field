# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-unitfield',
    version='0.0.2',
    author=u'Christian Kohout',
    author_email='ck@getaweb.at',
    packages=find_packages(),
    url='https://github.com/mbourqui/django-unitfield',
    license='UNLICENSE, see UNLICENSE.txt',
    description='a new field inherited from FloatField with a custom widget' + \
                ' that allows unit conversion',
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
)
