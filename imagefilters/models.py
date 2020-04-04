from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    my_username = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.my_username


class UserOriginalImage(models.Model):

    original_image_name = models.CharField(max_length=200, null=True)
    the_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)

    original_image = models.ImageField(null=True, upload_to="original_images/")
    creation_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.original_image_name


class UserEditedImage(models.Model):

    edited_image_name = models.CharField(max_length=200, null=True)
    original_image = models.ForeignKey(UserOriginalImage, on_delete=models.DO_NOTHING, null=True)
    edited_image = models.ImageField(null=True, upload_to="edited_images")
    creation_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.edited_image_name
