# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from pprint import pprint
from django.test import TestCase
from mock import Mock

from rest_framework_webdav.serializers import *
from rest_framework_webdav.resources import *
from .resources import MockResource

class TestPropfindSerializer(TestCase):

    def setUp(self):
        pass

    def test_request(self):
        pass

class TestMultiStatusSerializer(TestCase):

    def setUp(self):
        #FIXME use proper mock objects
        class TestDirFSResource(MetaEtagMixIn, BaseFSDavResource):
            root = os.path.dirname(os.path.realpath(__file__))

            def __str__(self):
                return "<Resource object for %s>" % self.get_abs_path()

        self.resource = TestDirFSResource('/')

    def test_1(self):
        # TODO proper testing, currently this is used to check the output by eye
        expect = 'asdasd'
        ser1 = MultistatusSerializer(instance=self.resource, context={
            'depth': 1,
            })
        rep1 = ser1.data
        pprint(rep1)
        print('-----------')
