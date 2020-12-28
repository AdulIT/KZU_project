from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.profile_url = reverse('profile')
		self.ProfilePage = reverse('profile')


	def test_profile_GET(self):
		response = self.client.get(self.profile_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/profile.html')

	def test_Profile_Page_GET(self):
		response = self.client.get(self.ProfilePage)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/profile.html')

