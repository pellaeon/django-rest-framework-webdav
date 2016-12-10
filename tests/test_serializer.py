# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
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
        class TestDirFSResource(BaseFSDavResource):
            root = os.path.dirname(os.path.realpath(__file__))

            def __str__(self):
                return "<Resource object for %s>" % self.get_abs_path()

        self.resource = TestDirFSResource('/')

    def test_1(self):
        # TODO proper testing, currently this is used to check the output by eye
        expect = 'asdasd'
        #print(self.resource.get_path())
        ser1 = MultistatusSerializer(instance=self.resource, context={
            'requested_resource': self.resource,
            'depth': 1,
            })
        rep1 = ser1.data
        print(rep1)
        print('-----------')

        #print(dir(ser1.fields['responses']))
        #ser1.fields['responses'].get_descendants()
        #print(ser1.fields['responses'].descendants[0].get_path())
        #print(ser1.fields['responses'].descendants[0].to_representation())
        #print(ser1.fields['responses'].descendants[0].instance)
        #print(ResponseSerializer.to_representation(ser1.fields['responses'].descendants[0]))
