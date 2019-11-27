import unittest
from django.test import TestCase

from blogsite.settings.production import STATIC_ROOT
from blogsite.settings.base import BASE_DIR
from blogsite.settings.utils import static_root, identifies_production_or_local

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
        STATIC_ROOT_STAGE = '/home/gregstage/staging.gregshepley.com/public/static'
        STATIC_ROOT_LOCAL = '/home/gregshepley/code/projects/blogsite_project/blogsite'
        BASE_URL_LOCAL = '/Users/gregshepley/code/projects/blogsite_project/blogsite'
        BASE_URL_LIVE = '/home/gregname/gregshepley.com/blogsite_project'
        BASE_URL_STAGING = '/home/gregstage/staging.gregshepley.com/blogsite_project/blogsite'

        self.assertEqual(
            static_root(BASE_DIR_LIVE),
            STATIC_ROOT_LIVE
        )
        self.assertEqual(
        	static_root(BASE_URL_STAGING),
        	STATIC_ROOT_STAGE
        	)

        self.assertEqual(
        	static_root(BASE_DIR_LOCAL),
        	STATIC_ROOT_LOCAL)

    def test_static_root_correct_for_staging(self):
        STATIC_ROOT_STAGE = '/home/gregstage/staging.gregshepley.com/public/static'
