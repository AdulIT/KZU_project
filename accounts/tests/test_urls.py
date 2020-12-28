from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import LoginView, RegisterView, ProfilePage
from django.contrib.auth.views import LogoutView, PasswordResetView

class TestUrls(SimpleTestCase):

	def test_login_url_resolves(self):
		url = reverse('login')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, LoginView)

	def test_logout_url_resolves(self):
		url = reverse('logout')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, LogoutView)

	def test_password_reset_url_resolves(self):
		url = reverse('password_reset')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, PasswordResetView)

	def test_register_url_resolves(self):
		url = reverse('register')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, RegisterView)

	def test_profile_url_resolves(self):
		url = reverse('profile')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class, ProfilePage)