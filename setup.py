from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from setuptools import setup, find_packages


version = '1.0.5.dev0'

setup(
    author='Tim Martin',
    author_email='tim.martin@vertical-knowledge.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    description='An extension for ripozo that brings HATEOAS/REST/Hypermedia apis to flask',
    extras_require={
        'examples': [
            'flask-ripozo',
            'Flask-SQLAlchemy',
            'pypermedia',
            'ripozo-sqlalchemy'
        ]
    },
    install_requires=[
        'ripozo',
        'Flask'
    ],
    name='flask-ripozo',
    packages=find_packages(exclude=['*_tests*', 'examples', 'profiling']),
    test_suite='flask_ripozo_tests',
    tests_require=[
        'unittest2',
        'mock',
        'six',
        'tox'
    ],
    url='http://flask-ripozo.readthedocs.org/',
    version=version
)
