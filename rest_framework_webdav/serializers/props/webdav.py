"""
All props specified by RFC 4918
"""

from .base import *

class Getlastmodified(BaseProp):
    name = 'getlastmodified'
    live = True
    status = "HTTP/1.1 200 OK"
    value = None #TODO remove
    namespace = Namespace(slug='d', identifier='DAV:')

    def to_representation(self, obj):
        return obj.getlastmodified
