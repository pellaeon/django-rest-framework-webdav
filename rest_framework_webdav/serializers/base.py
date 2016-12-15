from __future__ import unicode_literals
from collections import OrderedDict

from rest_framework.serializers import Serializer

from rest_framework_webdav.namespaces import DAVNS

class WebDAVResponseSerializer(Serializer):

    depth = None

    def __init__(self, depth=1, *args, **kwargs):
        """
        depth: requested depth from client
        """
        # TODO use context.depth
        self.depth = depth
        super(WebDAVResponseSerializer, self).__init__(**kwargs)

    def to_representation(self, obj):
        ns_ret = OrderedDict()
        ret = super(WebDAVResponseSerializer, self).to_representation(obj)
        for key, val in ret.items():
            ns_ret[DAVNS.prepend(key)] = val
        return ns_ret

class WebDAVRequestSerializer(Serializer):

    depth = None
    # TODO
