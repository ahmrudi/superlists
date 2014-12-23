from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout

# Create your tests here.

from notes.views import home_page, login_user, logout_user, sign_up

class NewNotesTest(TestCase):

	def test_notes_home_page(self):
		# masuk ke home page notes
		notes = resolve('/notes/')
		# cek function home_page
		self.assertEqual(notes.func, home_page)

class LoginTest(TestCase):
	
	def test_login_page(self):
		username = 'budy'
		password = 'siedoer91'
		response = self.client.post('/login/',
			data={'username':username, 'password':password})
		self.assertRedirects(response, '/error/')

class LogoutTest(TestCase):
	
	def test_logout_page(self):
		logout_page = resolve('/logout/')
		self.assertEqual(logout_page.func, logout_user)

class SignupTest(TestCase):
	
	def test_sign_up_page(self):
		signup = resolve('/sign-up/')
		self.assertEqual(signup.func, sign_up)
		