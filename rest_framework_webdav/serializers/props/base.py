from collections import namedtuple

from rest_framework.serializers import Serializer

Namespace = namedtuple('Namespace', ['slug', 'identifier'])

class BaseProp(Serializer):
    name = 'baseprop'
    live = True
    status = None
    value = None
    namespace = Namespace(slug='d', identifier='DAV:')

    def to_representation(self, obj):
        raise NotImplementedError("You shouldn't use BaseProp directly. Subclass and implement to_representation().")
