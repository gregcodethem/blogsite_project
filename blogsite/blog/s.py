import unittest
from utils import identifies_production_or_local
BASE_URL_LOCAL = '/Users/gregshepley/code/projects/blogsite_project/blogsite'
BASE_URL_LIVE = '/home/gregname/gregshepley.com/blogsite_project'
BASE_URL_LOCAL = '/home/gregstage/staging.gregshepley.com/blogsite_project/blogsite'

list = BASE_URL_LOCAL.split('/')
print(list)

class SettingsTest(unittest.TestCase):

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

if __name__ == '__main__':  
    unittest.main(warnings='ignore')