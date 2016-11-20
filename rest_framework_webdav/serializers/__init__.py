from __future__ import unicode_literals

from rest_framework.serializers import Serializer
from .fields import *

class ResponseSerializer(Serializer):
    """
    A serializer that recursively generates nested fields from BaseResource
    into primitive representations.

    We expect the object sended here as a single resource.

    Automatically add missing required properties to object
    http://www.webdav.org/specs/rfc4918.html#dav.properties
    """
    def to_representation(self, obj):
        """
        obj must be an instance of BaseResource
        """
        output = {}
        for attribute_name in dir(obj):
            attribute = getattr(obj, attribute_name)
            if attribute_name('_'):
                # Ignore private attributes.
                pass
            elif hasattr(attribute, '__call__'):
                # Ignore methods and other callables.
                pass
            elif isinstance(attribute, (str, int, bool, float, type(None))):
                # Primitive types can be passed through unmodified.
                output[attribute_name] = attribute
            elif isinstance(attribute, list):
                # Recursively deal with items in lists.
                output[attribute_name] = [
                    self.to_representation(item) for item in attribute
                ]
            elif isinstance(attribute, dict):
                # Recursively deal with items in dictionaries.
                output[attribute_name] = {
                    str(key): self.to_representation(value)
                    for key, value in attribute.items()
                }
            else:
                # Force anything else to its string representation.
                output[attribute_name] = str(attribute)

        return output
    
class MultistatusSerializer(Serializer):
    """
    <!ELEMENT multistatus (response*, responsedescription?)  >

    http://www.webdav.org/specs/rfc4918.html#ELEMENT_multistatus
    """
    responses = ResponseSerializer(many=True)
    responsedescription = ResponsedescriptionField(allow_blank=True)


class PropfindSerializer(Serializer):
    """
    <!ELEMENT propfind ( propname | (allprop, include?) | prop ) >

    http://www.webdav.org/specs/rfc4918.html#ELEMENT_propfind
    """

    propname = PropnameField(allow_blank=True)
    allprop = AllpropField(allow_blank=True)
    include = IncludeSerializer(allow_blank=True)
    prop = PropSerializer(allow_blank=True)

