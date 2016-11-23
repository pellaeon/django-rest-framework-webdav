from __future__ import unicode_literals

from rest_framework.fields import CharField

from rest_framework_webdav.serializers import WebDAVRequestSerializer
#from rest_framework_webdav.fields import *

"""
Elements that only appear in WebDAV client requests

Only to_internal_value() needs to be implemented.
"""

class PropfindSerializer(WebDAVRequestSerializer):
    """
    <!ELEMENT propfind ( propname | (allprop, include?) | prop ) >

    http://www.webdav.org/specs/rfc4918.html#ELEMENT_propfind
    """

    #propname = PropnameField(allow_blank=True)
    #allprop = AllpropField(allow_blank=True)
    #include = IncludeSerializer(allow_blank=True)
    #prop = PropSerializer(allow_blank=True)
    propname = CharField(allow_blank=True)
    allprop = CharField(allow_blank=True)
    include = CharField(allow_blank=True)
    prop = CharField(allow_blank=True)

    def to_representation(self, obj):
        raise NotImplementedError()
