"""Setuptools entry point."""
import codecs
import os

from setuptools import setup


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Internet',
    'Environment :: Web Environment',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Framework :: Django',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.10',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
]

dirname = os.path.dirname(__file__)

long_description = codecs.open(os.path.join(dirname, 'README.md'), encoding='utf-8').read()

setup(
    name='django-http-method',
    version="0.2.1",
    description='Provide a workaround to use different method from GET or POST inside HTML forms ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Coumes Quentin',
    author_email='coumes.quentin@gmail.com',
    url='https://github.com/qcoumes/django-http-method',
    packages=['django_http_method', 'django_http_method.templatetags'],
    install_requires=[],
    classifiers=CLASSIFIERS,
)
