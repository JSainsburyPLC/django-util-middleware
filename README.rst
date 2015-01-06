Django Util Middleware
======================

Utility middleware for use across projects which use Django or Django-REST-Framework.

Middleware
----------

JSON Exceptions
```````````````

Returns Python exceptions as a JSON response, in place of the standard Django HTML response, in the following format::

  {
  "ERROR": "[the error message as a single line]",
  "TRACEBACK": "[the multi-line traceback]"
  }

Timestamp Header
````````````````

Adds a ``Timestamp`` header to all responses, useful for comparing out-of-sync responses to filter for newest.
