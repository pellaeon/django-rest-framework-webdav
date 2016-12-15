"""
All props specified by RFC 4918
"""

from .base import *

from rest_framework.fields import CharField
from rest_framework.serializers import Serializer

from rest_framework_webdav.serializers.utils import find_subclasses
from rest_framework_webdav.namespaces import DAVNS

class Getlastmodified(BaseProp, CharField):
    # TODO refactor resource class, resource class should return datetime object,
    # and let this field convert it to string.
    live = True
    status = "HTTP/1.1 200 OK"
    # source = 'getlastmodified' # same as name so don't specify

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
        ret = super(Resourcetype, self).to_representation(obj)
        if obj.is_collection:
            ret[DAVNS.prepend('collection')] = None
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
        for resourcetype_cls in find_subclasses(cls=BaseResourcetypeChild):
            # resourcetype classes are always passed entire resobj instance
            fields[resourcetype_cls.__name__.lower()] = resourcetype_cls(source='*')
        return fields
