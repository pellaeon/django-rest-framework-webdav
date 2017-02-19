"""
All props specified by RFC 4918
"""

from .base import *

from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import Serializer

from rest_framework_webdav.serializers.utils import find_subclasses
from rest_framework_webdav.namespaces import DAVNS
from rest_framework_webdav.settings import webdav_api_settings

class Getlastmodified(BaseProp, CharField):
    # TODO refactor resource class, resource class should return datetime object,
    # and let this field convert it to string.
    live = True
    status = "HTTP/1.1 200 OK"

class Getetag(BaseProp, CharField):
    live = True
    status = "HTTP/1.1 200 OK"

class Resourcetype(BaseProp, Serializer):
    """
    http://www.webdav.org/specs/rfc4918.html#PROPERTY_resourcetype
    """
    live = True
    status = "HTTP/1.1 200 OK"
    needed_source = '*'

    def to_representation(self, obj):
        fielddict = super(Resourcetype, self).to_representation(obj)

        ret = {}
        # use field values as return dict keys
        for key, val in fielddict.items():
            if val == None:
                continue
            ret[val] = None
        return ret

    def get_fields(self):
        """
        Fields are determined dynamically, because <resourcetype> can contain
        custom elements from other namespaces.
        This will be invoked by @property fields() ,
        fields() will set _fields as a BindingDict, which will .bind() the field
        when you __setitem__()
        """
        fields = {}
        for resourcetype_cls in webdav_api_settings.RESOURCETYPES:
            """
            <resourcetype> children don't have keys, only values, but
            field values won't be available until to_representation is called,
            so we can't set the field name to value just yet, we'll do it in
            to_representation.
            """
            fields[resourcetype_cls.__name__.lower()] = resourcetype_cls(source='*')
        return fields

class Creationdate(BaseProp, CharField):
    live = True
    status = "HTTP/1.1 200 OK"

class Displayname(BaseProp, CharField):
    live = True
    status = "HTTP/1.1 200 OK"

class Getcontenttype(BaseProp, CharField):
    live = True
    status = "HTTP/1.1 200 OK"
    needed_source = 'content_type'

class Getcontentlength(BaseProp, IntegerField):
    live = True
    status = "HTTP/1.1 200 OK"
