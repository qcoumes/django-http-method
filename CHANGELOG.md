----------------------------

# Changelog


#### 1.0.1

* Now use `yaml.safe_load()` instead of `yaml.load()`
* Added python 3.7 and django 2.1 to test matrix


#### 1.0.0

* Initial release for python3.4+ and django1.8, 1.10, 1.11 and 2.0+ 


#### 0.4.0

* Will now search for parameters in body for methods PUT and PATCH
* Method will default to request.method if '_method' parameter was not found


#### 0.3.2

* Added end slash '/' at the end of HTML input in templatetags


#### 0.3.0

* Removing '_method' from request parameters
