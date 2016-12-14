from collections import namedtuple

from rest_framework.serializers import Serializer

Namespace = namedtuple('Namespace', ['slug', 'identifier'])

class BaseProp(object):
    live = True
    status = None
    namespace = Namespace(slug='d', identifier='DAV:')
    # what source you need when ResponseSerializer initializes this Field,
    # will be fed into source= when init, use None if you want to use the
    # attribute on resobj that has the same name as this class's name.
    # Use '*' to specify this field needs an entire resobj
    needed_source = None
