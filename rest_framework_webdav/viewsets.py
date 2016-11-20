from __future__ import unicode_literals

from rest_framework.viewsets import GenericViewSet
from rest_framework.settings import api_settings

from .serializers import WebDAVSerializer
from rest_framework_xml.renderers import XMLRenderer

class GenericDavViewSet(GenericViewSet):
    """
    Generic WebDAV viewset

    Provides a viewset set with WebDAV renderers, parsers, metadata classes
    """

    # override from django.views.View , list of all possible methods
    http_method_names = ['get', 'put', 'lock', 'unlock', 'propfind',
            'proppatch', 'delete', 'head', 'options', 'mkcol', 'copy', 'move',
            ]

    renderer_classes = tuple(XMLRenderer) + api_settings.DEFAULT_RENDERER_CLASSES
    parser_classes = api_settings.DEFAULT_PARSER_CLASSES
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    throttle_classes = api_settings.DEFAULT_THROTTLE_CLASSES
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    content_negotiation_class = api_settings.DEFAULT_CONTENT_NEGOTIATION_CLASS
    metadata_class = api_settings.DEFAULT_METADATA_CLASS
    versioning_class = api_settings.DEFAULT_VERSIONING_CLASS

    serializer_class = WebDAVSerializer

