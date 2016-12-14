from __future__ import unicode_literals

from rest_framework.serializers import Serializer

class WebDAVResponseSerializer(Serializer):

    depth = None

    def __init__(self, depth=1, *args, **kwargs):
        """
        depth: requested depth from client
        """
        # TODO use context.depth
        self.depth = depth
        super(WebDAVResponseSerializer, self).__init__(**kwargs)

class WebDAVRequestSerializer(Serializer):

    depth = None
    # TODO
