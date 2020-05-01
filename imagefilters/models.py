from django.db import models
from django.contrib.auth.models import User
from .conventional_image_filters import *

# Create your models here.

class MyUser(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    my_username = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.my_username


class UserOriginalImage(models.Model):

    original_image_name = models.CharField(max_length=200, null=True)
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)

    original_image = models.ImageField(null=True, upload_to="original_images/")
    creation_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.original_image_name

    def gaussian_filter(self):
        img_content = gaussian_image_filter(self.original_image)
        UserEditedImage.objects.create(original_image=self, edited_image=img_content, edited_image_name='edited_img_gaussian')

    def edging_filter(self):
        img_content = edging_image_filter(self.original_image)
        UserEditedImage.objects.create(original_image=self, edited_image=img_content, edited_image_name='edited_image_edging')

    def rgb2gray_filter(self):
        img_content = rgb_to_gray(self.original_image)
        UserEditedImage.objects.create(original_image=self, edited_image=img_content, edited_image_name='edited_image_rgb2gray')


class UserEditedImage(models.Model):

    FILTER_TYPES = (
        ('gaussian', 'gaussian'),
        ('edging', 'edging')
    )

    edited_image_name = models.CharField(max_length=200, null=True)
    original_image = models.ForeignKey(UserOriginalImage, on_delete=models.DO_NOTHING, null=True)
    edited_image = models.ImageField(null=True, upload_to="edited_images")
    creation_date = models.DateTimeField(auto_now=True, null=True)

    filter_type = models.CharField(max_length=200, null=True, choices=FILTER_TYPES)

    def __str__(self):
        return self.edited_image_name
