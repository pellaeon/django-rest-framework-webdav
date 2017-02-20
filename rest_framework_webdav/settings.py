# -*- coding: utf-8 -*-
from django.conf import settings
from django.test.signals import setting_changed

from rest_framework.settings import APISettings

from pprint import pprint

USER_SETTINGS = getattr(settings, 'REST_FRAMEWORK_WEBDAV', None)

DEFAULTS = {
    'XML_NAMESPACES': ['rest_framework_webdav.namespaces.DAVNS'],
    'RESOURCETYPES': ['rest_framework_webdav.serializers.props.resourcetype.IscollectionResourceType'],
}

IMPORT_STRINGS = [
    'XML_NAMESPACES',
    'RESOURCETYPES',
]

webdav_api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)

def reload_api_settings(*args, **kwargs):
    global webdav_api_settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == 'REST_FRAMEWORK_WEBDAV':
        webdav_api_settings = APISettings(value, DEFAULTS, IMPORT_STRINGS)
        print('%s: %s' % (kwargs['enter'], webdav_api_settings.RESOURCETYPES))


setting_changed.connect(reload_api_settings)
