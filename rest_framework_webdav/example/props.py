from rest_framework.fields import CharField
from rest_framework_webdav.serializers.props.resourcetype.base import BaseResourcetypeChild
from .namespaces import PHOTONS

class PhotoResourceType(BaseResourcetypeChild, CharField):
    namespace = PHOTONS

    def to_representation(self, obj):
        if obj.is_collection:
            return self.namespace.prepend('album')
        elif obj.content_type.startswith('image/'):
            return self.namespace.prepend('photo')
        else:
            return self.namespace.prepend('unknown')
