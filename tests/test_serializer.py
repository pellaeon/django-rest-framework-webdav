# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
        self.resource = MockResource('/path/屯/nnn')
        self.resource1 = MockResource('/path/屯/nnn/1')
        self.resource2 = MockResource('/path/屯/nnn/2')
        MockResource.get_children = Mock(return_value=[self.resource1, self.resource2])

    def test_1(self):
        expect = 'asdasd'
        #print(self.resource.get_path())
        ser1 = MultistatusSerializer(instance=self.resource, context={
            'requested_resource': self.resource,
            'depth': 1,
            })
        rep1 = ser1.data
        print(rep1)
        print('-----------')

        print(dir(ser1.fields['responses']))
        #ser1.fields['responses'].get_descendants()
        #print(ser1.fields['responses'].descendants[0].get_path())
        #print(ser1.fields['responses'].descendants[0].to_representation())
        #print(ser1.fields['responses'].descendants[0].instance)
        #print(ResponseSerializer.to_representation(ser1.fields['responses'].descendants[0]))
        print(ser1.fields['responses'].descendants)
