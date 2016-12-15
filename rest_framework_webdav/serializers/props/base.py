from rest_framework.serializers import Serializer

from rest_framework_webdav.namespaces import DAVNS

class BaseProp(object):
    """
    All prop serializers must subclass BaseProp to register themselves.
    Then ResponseSerializer will call every prop serializer to propagate values.
    """
    live = True
    status = None
    namespace = DAVNS
    # what source you need when ResponseSerializer initializes this Field,
    # will be fed into source= when init, use None if you want to use the
    # attribute on resobj that has the same name as this class's name.
    # Use '*' to specify this field needs an entire resobj
    needed_source = None

class BaseResourcetypeChild(object):
    """
    All custom <resourcetype> child elements must subclass BaseResourcetypeChild
    to register.
    resourcetype classes are always passed entire resobj instance.
    """
    namespace = DAVNS
