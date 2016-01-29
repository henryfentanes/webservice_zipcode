from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    '''GET / must return status code 200'''
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        ''' Must use core/index.html'''
        self.assertTemplateUsed(self.response, 'core/index.html')
