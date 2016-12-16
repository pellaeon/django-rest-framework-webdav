# -*- coding: utf-8 -*-
from django.conf import settings

from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'REST_FRAMEWORK_WEBDAV', None)

DEFAULTS = {
    'XML_NAMESPACES': ['rest_framework_webdav.namespaces.DAVNS'],
}

IMPORT_STRINGS = [
    'XML_NAMESPACES',
]

webdav_api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)