from __future__ import unicode_literals

from rest_framework.fields import CharField, URLField, ListField
from rest_framework.serializers import ListSerializer

from rest_framework_webdav.serializers import WebDAVResponseSerializer
#from rest_framework_webdav.fields import *
from rest_framework_webdav.resources import BaseResource

"""
Elements that only appear in WebDAV client requests

Only to_representation() needs to be implemented.
"""

class PropstatSerializer(WebDAVResponseSerializer):
    """
    <!ELEMENT propstat (prop, status, error?, responsedescription?) >

    Determines each prop's status code, group them by status code,
    to_representation() returns a list of <propstat>, each propstat in the list
    contain the props that are with the same status code.
    """

    #prop = PropSerializer()
    prop = CharField(source='testing_prop') # FIXME PoC

    def testing_prop(self):
        return 'blabla'

class ResponseListSerializer(ListSerializer):

    def to_representation(self, obj):
        # obj is the Resource object of client requested path,
        # we won't use it here, we use response_objects instead
        ret = []
        for resp_obj in self.get_response_objects():
            ret.append(self.child.to_representation(resp_obj))

        return ret

    def get_response_objects(self):
        # Note that in WebDAV all response objects are flattened into a list, regardless of Depth
        assert isinstance(self.context.get('depth'), int)
        return list(self.context.get('requested_resource').get_descendants(
            depth=self.context.get('depth'))
            )

class ResponseSerializer(WebDAVResponseSerializer):
    """
    <!ELEMENT response (href, ((href*, status)|(propstat+)), 
                        error?, responsedescription? , location?) >

    Automatically add missing required properties to object
    http://www.webdav.org/specs/rfc4918.html#dav.properties
    """

    class Meta:
        list_serializer_class = ResponseListSerializer

    href = ListField(child=URLField(max_length=None))
    status = CharField(required=False)
    propstat = PropstatSerializer(many=True, source='*')

    #maybe delete this
    def to_representation(self, resource):
        assert isinstance(resource, BaseResource)

        # this will in turn call to_representation() on every field
        output = super(ResponseSerializer, self).to_representation(self.instance)

        return output
    
class MultistatusSerializer(WebDAVResponseSerializer):
    """
    <!ELEMENT multistatus (response*, responsedescription?)  >

    http://www.webdav.org/specs/rfc4918.html#ELEMENT_multistatus
    """
    # http://www.django-rest-framework.org/api-guide/fields/#source
    responses = ResponseSerializer(many=True, source='*')
    responsedescription = CharField(required=False)

    def __init__(self, depth=0, *args, **kwargs):
        if not isinstance(kwargs['instance'], BaseResource):
            raise TypeError("You need to feed in an instance of BaseResource "
                "like this: MultistatusSerializer(instance=res_obj) ")

        # because instance is not passed to list serializer
        #self.context.set('requested_resource', self.context.get('requested_resource') or kwargs['instance'])
        super(MultistatusSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, obj):
        #self.fields['responses'].depth = self.depth
        super(MultistatusSerializer, self).to_representation(obj)
