import unittest
from django.test import TestCase

from blogsite.settings.production import STATIC_ROOT

# Create your tests here.
class SettingsTest(TestCase):

	def static_root_correct_for_live_test(self):
		STATIC_ROOT_LIVE = '/home/gregname/gregshepley.com/public/static'
		self.assertEqual(STATIC_ROOT, STATIC_ROOT_LIVE)

	def smoking_test():
		self.assertEqual(1,2)