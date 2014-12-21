# file lists/test.py
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		# masuk kedalam url root
		found = resolve('/')
		# apakah ada function home_page disitu?
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		# memintta object halaman
		request = HttpRequest()
		# yang ada di home page
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)
		self.assertTrue(response.content.strip().startswith(b'<html>'))
		# dengan judul To-Do lists
		self.assertIn(b'<title>To-Do lists</title>', response.content)
		# dan diakhiri dengan kode html pula
		self.assertTrue(response.content.strip().endswith(b'</html>'))
