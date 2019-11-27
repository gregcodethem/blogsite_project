import unittest
from django.test import TestCase

from blogsite.settings.production import STATIC_ROOT

# Create your tests here.
class SettingsTest(TestCase):

	def test_static_root_correct_for_live(self):
		STATIC_ROOT_LIVE = '/home/gregname/gregshepley.com/public/static'
		self.assertEqual(STATIC_ROOT, STATIC_ROOT_LIVE)

	def test_static_root_correct_for_staging(self):
		STATIC_ROOT_STAGE = '/home/gregstage/staging.gregshepley.com/public/static'

