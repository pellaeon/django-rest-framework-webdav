"""
All props specified by RFC 4918
"""

from .base import *

class WebdavNamespace(PropNamespace):
    slug = 'd'
    identifier = 'DAV:'

    def prop_getlastmodified(self):
        return self.resource.getlastmodified
