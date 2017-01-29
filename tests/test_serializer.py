# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from pprint import pprint
from django.test import TestCase
from mock import Mock

from rest_framework_webdav.serializers import *
from rest_framework_webdav.resources import *
from .resources import MockResource

from rest_framework_webdav.renderers import WebDAVXMLRenderer
from rest_framework_webdav.serializers.utils import ElementList

class TestPropfindSerializer(TestCase):

    def setUp(self):
        pass

    def test_request(self):
        pass

class TestResponseSerializers(TestCase):

    def setUp(self):
        #FIXME use proper mock objects
        class TestDirFSResource(MetaEtagMixIn, BaseFSDavResource):
            root = os.path.dirname(os.path.realpath(__file__))

            def __str__(self):
                return "<Resource object for %s>" % self.get_abs_path()

        self.resource = TestDirFSResource('/')

        ser1 = MultistatusSerializer(instance=self.resource, context={
            'depth': 1,
            })
        self.rep1 = ser1.data

    def test_multistatus(self):
        self.assertIsNone(self.rep1['d:responsedescription'])
        self.assertIsInstance(self.rep1['d:response'], ElementList)

        # print actual data for humans to check
        renderer = WebDAVXMLRenderer()
        print(renderer.render(self.rep1))
        #pprint(self.rep1)
        print('-----------')

    def test_response(self):
        self.assertEqual(self.rep1['d:response'][0]['d:href'], '/')
        self.assertIsInstance(self.rep1['d:response'][0]['d:propstat'], dict)

    def test_propstat(self):
        self.assertEqual(self.rep1['d:response'][0]['d:href'], '/')
        self.assertIsInstance(self.rep1['d:response'][0]['d:propstat'], dict)
