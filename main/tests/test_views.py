from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.home_url = reverse('home')
		self.about_url = reverse('about')
		self.city_url = reverse('city')

	def test_index_GET(self):
		response = self.client.get(self.home_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/index.html')

	def test_about_GET(self):
		response = self.client.get(self.about_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/about.html')

	def test_city_GET(self):
		response = self.client.get(self.city_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/city.html')