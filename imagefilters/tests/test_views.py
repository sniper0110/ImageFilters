from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Group #User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.contrib.auth import login

import os

from ..models import MyUser, UserOriginalImage, UserEditedImage


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.login_url = reverse('imagefilters:loginPage')
        self.register_url = reverse('imagefilters:registerPage')
        self.image_filtering_options_url = reverse('imagefilters:filtering_options', args=['2'])

        User = get_user_model()
        self.user = User.objects.create_user('test', 'test@gmail.com', 'test')
        self.client.login(username='test', password='test')

        self.myuser = MyUser.objects.create(
            user=self.user,
        )

        dirname = os.path.dirname(__file__)
        relative_path = 'sample_testing_files/sample_img.jpg'
        sample_img_path = os.path.join(dirname, relative_path)

        self.sample_loaded_image = SimpleUploadedFile(name='test_image.jpg', content=open(sample_img_path, 'rb').read(),
                                                      content_type='image/jpeg')

        self.sample_original_image = UserOriginalImage.objects.create(
            id='2',
            myuser=self.myuser,
            original_image=self.sample_loaded_image,
            original_image_name='sample_original_image'
        )



    def test_login_page_view_GET(self):

        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'imagefilters/login_page.html')


    def test_register_page_view_GET(self):

        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'imagefilters/register_page.html')


    def test_image_filtering_options_view_GET(self):

        response = self.client.get(self.image_filtering_options_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'imagefilters/image_filtering_options.html')








