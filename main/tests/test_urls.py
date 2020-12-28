from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import index, about, city


class TestUrls(SimpleTestCase):

	def test_home_url_resolves(self):
		url = reverse('home')
		print(resolve(url))
		self.assertEquals(resolve(url).func, index)

	def test_about_url_resolves(self):
		url = reverse('about')
		print(resolve(url))
		self.assertEquals(resolve(url).func, about)

	def test_city_url_resolves(self):
		url = reverse('city')
		print(resolve(url))
		self.assertEquals(resolve(url).func, city)