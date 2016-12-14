"""
All props specified by RFC 4918
"""

from .base import *

from rest_framework.fields import CharField

class Getlastmodified(BaseProp, CharField):
    # TODO refactor resource class, resource class should return datetime object,
    # and let this field convert it to string.
    live = True
    status = "HTTP/1.1 200 OK"
    namespace = Namespace(slug='d', identifier='DAV:')
    # source = 'getlastmodified' # same as name so don't specify
