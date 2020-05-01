from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import *


class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('imagefilters:loginPage')
        self.assertEqual(resolve(url).func, login_page)

    def test_register_url_is_resolved(self):
        url = reverse('imagefilters:registerPage')
        self.assertEqual(resolve(url).func, register_page)

    def test_home_page_url_is_resolved(self):
        url = reverse('imagefilters:home_page')
        self.assertEqual(resolve(url).func, user_home_page)

    def test_filtering_options_url_is_resolved(self):
        url = reverse('imagefilters:filtering_options', args=['1'])
        self.assertEqual(resolve(url).func, image_filtering_options)

    def test_filter_image_form_url_is_resolved(self):
        url = reverse('imagefilters:filter_image_form', args=['1'])
        self.assertEqual(resolve(url).func, filter_image_form)

    def test_gaussian_filter_url_is_resolved(self):
        url = reverse('imagefilters:gaussian_filter', args=['1'])
        self.assertEqual(resolve(url).func, apply_gaussian_filter)

    def test_edging_filter_url_is_resolved(self):
        url = reverse('imagefilters:edging_filter', args=['1'])
        self.assertEqual(resolve(url).func, apply_edging_filter)

    def test_rgb2gray_filter_url_is_resolved(self):
        url = reverse('imagefilters:rgb2gray_filter', args=['1'])
        self.assertEqual(resolve(url).func, apply_rgb2gray_filter)