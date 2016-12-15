from __future__ import unicode_literals

from rest_framework.fields import *
from rest_framework.serializers import ListSerializer

from rest_framework_webdav.serializers import WebDAVResponseSerializer
from rest_framework_webdav.resources import BaseResource
# import all prop class so find_subclasses can find them
from rest_framework_webdav.serializers.props import *
# TODO we need a way to discover all third-party props and import them,
# so find_subclasses can find them.
from rest_framework_webdav.serializers.utils import find_subclasses

"""
Elements that only appear in WebDAV client requests

Only to_representation() needs to be implemented.
"""

class PropstatSerializer(WebDAVResponseSerializer):
    # TODO XML namespace for all serializers and fields
    """
    <!ELEMENT propstat (prop, status, error?, responsedescription?) >

    Determines each prop's status code, group them by status code,
    to_representation() returns a list of <propstat>, each propstat in the list
    contain the props that are with the same status code.
    """


    def to_representation(self, instance):
        """
        This implementation copies mostly from Serializer.to_representation() ,
        with the required additional feature: group fields (props) into
        propstat dictionaries.

        Sample output:
        {
            'HTTP/1.1 200 OK': [
                {'getlastmodified': 'Sat, 10 Dec 2016 16:31:16 -0000'}
            ]
        }

        TODO forgot prop, should be propstat -> prop -> getlastmodified
        TODO use _readable_fields just as in Serializer
        """
        out = {}
        for key, field in self.fields.items():
            try:
                attribute = field.get_attribute(instance) # get_attribute will check source='*'
            except SkipField:
                continue
            if field.status not in out:
                out[field.status] = []
            out[field.status].append({key: field.to_representation(attribute)})

        return out


    def get_fields(self):
        """
        Fields are determined dynamically.
        This will be invoked by @property fields() ,
        fields() will set _fields as a BindingDict, which will .bind() the field
        when you __setitem__()
        """
        fields = {}
        for prop_cls in find_subclasses(cls=BaseProp):
            fields[prop_cls.__name__.lower()] = prop_cls(source=prop_cls.needed_source) # initialize prop class
        return fields

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

    TODO permission
    """

    class Meta:
        list_serializer_class = ResponseListSerializer

    href = CharField(source='get_path')
    status = CharField(required=False)
    propstat = PropstatSerializer(source='*')
    
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

    def get_responsedescription(self, obj):
        # TODO overall description of all responses
        return None
