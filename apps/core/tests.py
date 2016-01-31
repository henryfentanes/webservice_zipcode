# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('home'))

    def test_get(self):
        '''GET / must return status code 200'''
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        ''' Must use core/index.html'''
        self.assertTemplateUsed(self.response, 'core/index.html')


class ZipCodeCreateTest(TestCase):
    def test_create_zipcode_scenario_1(self):
        response = self.client.post('/zipcode/', data={'zip_code': 14020260})
        self.assertEqual(201, response.status_code)
        self.assertTrue(response.data['state'])
        self.assertTrue(response.data['city'])
        self.assertTrue(response.data['neighborhood'])
        self.assertTrue(response.data['address'])

    def test_create_zipcode_scenario_2(self):
        response = self.client.post('/zipcode/', data={'zip_code': 14110000})
        self.assertEqual(201, response.status_code)
        self.assertTrue(response.data['state'])
        self.assertTrue(response.data['city'])
        self.assertFalse(response.data['neighborhood'])
        self.assertFalse(response.data['address'])

    def test_create_zipcode_scenario_3(self):
        response = self.client.post('/zipcode/', data={'zip_code': 20040972})
        self.assertEqual(201, response.status_code)
        self.assertTrue(response.data['state'])
        self.assertTrue(response.data['city'])
        self.assertTrue(response.data['neighborhood'])
        self.assertFalse(response.data['address'])

    def test_false_zipcode(self):
        response = self.client.post('/zipcode/', data={'zip_code': 1402260})
        self.assertEqual(404, response.status_code)
