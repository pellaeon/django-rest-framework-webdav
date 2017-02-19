from rest_framework.fields import CharField
from rest_framework_webdav.serializers.props.resourcetype.base import BaseResourcetypeChild

class IscollectionResourceType(BaseResourcetypeChild, CharField):
    """
    http://www.webdav.org/specs/rfc4918.html#PROPERTY_resourcetype
    """ 

    def to_representation(self, obj):
        if obj.is_collection:
            return self.namespace.prepend('collection')
        else:
            return None
