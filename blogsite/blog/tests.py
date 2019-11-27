import unittest
from django.test import TestCase

from blogsite.settings.production import STATIC_ROOT
from blogsite.settings.base import BASE_DIR
from bolgsite.settings.utils import identifies_production_or_local

# Create your tests here.
class SettingsTest(TestCase):

	def test_identifies_production_or_local(self):
		BASE_URL_LOCAL = '/Users/gregshepley/code/projects/blogsite_project/blogsite'
		BASE_URL_LIVE = '/home/gregname/gregshepley.com/blogsite_project'
		BASE_URL_STAGING = '/home/gregstage/staging.gregshepley.com/blogsite_project/blogsite'

		self.assertEqual(
			identifies_production_or_local(BASE_URL_LOCAL),
			'local')
		self.assertEqual(
			identifies_production_or_local(BASE_URL_LIVE),
			'production')
		self.assertEqual(
			identifies_production_or_local(BASE_URL_STAGING),
			'production')

		

	def test_static_root_correct_for_production(self):
		
		STATIC_ROOT_LIVE = '/home/gregname/gregshepley.com/public/static'
		
		self.assertEqual(
			static_root(BASE_DIR),
			STATIC_ROOT_LIVE)

	def test_static_root_correct_for_staging(self):
		STATIC_ROOT_STAGE = '/home/gregstage/staging.gregshepley.com/public/static'

