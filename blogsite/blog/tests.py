import unittest
from django.test import TestCase

from blogsite.settings.production import STATIC_ROOT

# Create your tests here.
class SettingsTest(TestCase):

	def static_root_correct_for_live(self):
		STATIC_ROOT_LIVE = '/home/gregname/gregshepley.com/public/static'
		self.assertEqual(STATIC_ROOT, STATIC_ROOT_LIVE)