from django.test import TestCase

# Create your tests here.
class SandTest(TestCase):

	def test_sand(self):
		self.assertEqual(1+1,2)
		self.assertEqual(1+3,5)