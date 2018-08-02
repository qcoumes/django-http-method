[![Build Status](https://travis-ci.org/qcoumes/django-http-method.svg?branch=master)](https://travis-ci.org/qcoumes/django-http-method)
[![PyPI Version](https://badge.fury.io/py/django-http-method.svg)](https://badge.fury.io/py/django-http-method)
[![Coverage Status](https://coveralls.io/repos/github/qcoumes/django-http-method/badge.svg?branch=master)](https://coveralls.io/github/qcoumes/django-http-method?branch=master)
[![Python 3.4+](https://img.shields.io/badge/python-3.4+-brightgreen.svg)](#)
[![Django 1.8, 1.10, 1.11, 2.0+](https://img.shields.io/badge/django-1.8%2C%201.10%2C%201.11%2C%202.0+-brightgreen.svg)](#)
[![License MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/qcoumes/gitcmd/blob/master/LICENSE)

# django-http-method
Provide a workaround to use different method than GET or POST inside HTML forms in django templates. Works only with Class Based View.

## Installation
From source code:

    python setup.py install

From pip:

    pip install django-http-method

## Usage

##### Add *django_http_method* to your settings.INSTALLED_APPS

```python
INSTALLED_APPS = (
    [...],
    django_http_method,
    [...],
)
```

##### Add the mixin to a CBV

```python
from django.views.generic import View
from django_http_method import HttpMethodMixin

class TestView(HttpMethodMixin, View):
	pass
```

##### In your template, load *http_method* and use `{% http_[method] %}` in your forms:
```html
{% load http_method %}

<form action="/" method="post">
    {% csrf_token %}
    {% http_put %}
    [...]
    <button type="submit">Send a PUT request</button>
</form>


<form action="/" method="post">
    {% csrf_token %}
    {% http_patch %}
    [...]
    <button type="submit">Send a PATCH request</button>
</form>
```

The corresponding method of your View will now be called. For instance, if `{% http_put %}` was used, then `TestView.put()` will be called and any request parameter will be in `request.PUT`.
