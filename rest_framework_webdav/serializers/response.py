from __future__ import unicode_literals

from rest_framework.fields import *
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

    descendants = []

    def to_representation(self, obj):
        if not self.descendants:
            self.get_descendants(obj)

        ret = []
        for descendant_field in self.descendants:
            ret.append(descendant_field.data)

        return ret

    def get_descendants(self, resource):
        # Note that in WebDAV all response objects are flattened into a list, regardless of Depth
        assert isinstance(self.context.get('depth'), int)
        for res_obj in resource.get_descendants(
                depth=self.context.get('depth')):
            print(res_obj)
            self.descendants.append(ResponseSerializer(instance=res_obj))

class ResponseSerializer(WebDAVResponseSerializer):
    """
    <!ELEMENT response (href, ((href*, status)|(propstat+)), 
                        error?, responsedescription? , location?) >

    Automatically add missing required properties to object
    http://www.webdav.org/specs/rfc4918.html#dav.properties
    """

    class Meta:
        list_serializer_class = ResponseListSerializer

    #href = ListField(child=URLField(max_length=None), source='get_path')
    href = SerializerMethodField()
    status = CharField(required=False)
    #propstat = PropstatSerializer(many=True, source='*')
    propstat = SerializerMethodField()

    #maybe delete this
    #def to_representation(self, resource):
    #    assert isinstance(resource, BaseResource)

    #    # this will in turn call to_representation() on every field
    #    output = super(ResponseSerializer, self).to_representation(self.instance)

    #    return output

    def get_href(self, obj):
        return self.instance.get_path()

    def get_propstat(self, obj):
        return "sssss"

    @property
    def data(self):
        return super(ResponseSerializer, self).data
    
class MultistatusSerializer(WebDAVResponseSerializer):
    """
    <!ELEMENT multistatus (response*, responsedescription?)  >

    http://www.webdav.org/specs/rfc4918.html#ELEMENT_multistatus

    Required init arguments:
    instance: resource object instance as originally requested by the client
    context['depth']: depth requested by client
    """
    # http://www.django-rest-framework.org/api-guide/fields/#source
    responses = ResponseSerializer(many=True, source='*')
    responsedescription = SerializerMethodField(required=False)

    def __init__(self, depth=0, *args, **kwargs):
        if not isinstance(kwargs['instance'], BaseResource):
            raise TypeError("You need to feed in an instance of BaseResource "
                "like this: MultistatusSerializer(instance=res_obj) ")

        super(MultistatusSerializer, self).__init__(*args, **kwargs)
        # because instance is not passed to list serializer
        self.context['requested_resource'] = self.context.get('requested_resource') or kwargs['instance']

    def get_responsedescription(self, obj):
        # TODO overall description of all responses
        return None
