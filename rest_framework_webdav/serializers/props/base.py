from rest_framework.serializers import Serializer

from rest_framework_webdav.namespaces import DAVNS

class BaseProp(object):
    """
    All prop serializers must subclass BaseProp to register themselves.
    Then ResponseSerializer will call every prop serializer to propagate values.

    Note:
    Usually you need to mix this class with a rest_framework `Field`
    class, this way rest_framework will fetch the field's value from the
    underlying resource object property that has the same name as your prop
    class name.
    See `serializers/props/webdav.py` for examples, such as `Getetag` prop, the
    value will be fetched from `res_obj.getetag`.
    """
    live = True
    status = None
    namespace = DAVNS
    # what source you need when ResponseSerializer initializes this Field,
    # will be fed into source= when init, use None if you want to use the
    # attribute on resobj that has the same name as this class's name.
    # Use '*' to specify this field needs an entire resobj
    needed_source = None
