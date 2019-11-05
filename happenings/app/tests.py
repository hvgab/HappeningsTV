from django.test import TestCase, SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse

from . import views

class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class TVTests(TestCase):

    def setUp(self):
        Tag.objects.create(name='Oslo')
        Tag.objects.create(name='Skien')
        
        Happening.objects.create(title='OsloEvent')
