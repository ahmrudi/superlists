# file lists/test.py
from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		# masuk kedalam url root
		found = resolve('/')
		# apakah ada function home_page disitu?
		self.assertEqual(found.func, home_page)
