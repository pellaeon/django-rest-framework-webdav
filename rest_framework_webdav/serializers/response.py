from __future__ import unicode_literals

from rest_framework_webdav.serializers import WebDAVResponseSerializer
from rest_framework_webdav.fields import *
from rest_framework_webdav.resources import BaseResource

"""
Elements that only appear in WebDAV client requests

Only to_representation() needs to be implemented.
"""

class ResponseSerializer(WebDAVResponseSerializer):
    """
    <!ELEMENT response (href, ((href*, status)|(propstat+)), 
                        error?, responsedescription? , location?) >

    Automatically add missing required properties to object
    http://www.webdav.org/specs/rfc4918.html#dav.properties
    """

    def to_representation(self, resource):
        assert isinstance(resource, BaseResource)

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
    
class MultistatusSerializer(WebDAVResponseSerializer):
    """
    <!ELEMENT multistatus (response*, responsedescription?)  >

    http://www.webdav.org/specs/rfc4918.html#ELEMENT_multistatus
    """
    # http://www.django-rest-framework.org/api-guide/fields/#source
    responses = ResponseSerializer(many=True, source='get_response_objects')
    responsedescription = ResponsedescriptionField(allow_blank=True)

    def __init__(self, *args, **kwargs):
        if not isinstance(kwargs['instance'], BaseResource):
            raise TypeError("You need to feed in an instance of BaseResource "
                "like this: MultistatusSerializer(instance=res_obj) ")
        super(MultistatusSerializer, self).__init__(*args, **kwargs)

    def get_response_objects(self):
        # TODO get response objects as a flat list, this will get fed into ResponseSerializer
        return [self.instance.get_descendants(depth=self.depth)]
