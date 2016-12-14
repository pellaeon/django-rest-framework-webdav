from collections import namedtuple

from rest_framework.serializers import Serializer

Namespace = namedtuple('Namespace', ['slug', 'identifier'])

class BaseProp(object):
    live = True
    status = None
    namespace = Namespace(slug='d', identifier='DAV:')
    # if true, ResponseSerializer will set source to entire resource object
    need_entire_resobj = False
