from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User, Group
from .models import MyUser, UserOriginalImage

import os


def generate_customer_profile(sender, instance, created, **kwargs):

    if not instance.is_staff:
        if created:

            try:
                group = Group.objects.get(name='FreemiumMember')
            except Group.DoesNotExist:
                print("\'FreemiumMember\' group does not exist!")
                pass
            else:
                instance.groups.add(group)
                username = instance.username
                email = instance.email

                MyUser.objects.create(user=instance, my_username=username, email=email)

                print("A user has been created (of type MyUser)")


def generate_upload_original_images_path(sender, instance, **kwargs):

    try:
        print("instance.original_image.upload_to = ", instance.original_image.upload_to)
        path_to_upload_images = os.path.join(instance.original_image.upload_to, instance.myuser.user.username)
        instance.original_image.upload_to = path_to_upload_images
    except:
        print("Could not set a new upload_to folder")
    else:
        print(f"New path for upload_to was generated : {instance.original_image.upload_to}")


post_save.connect(generate_customer_profile, sender=User)
pre_save.connect(generate_upload_original_images_path, sender=UserOriginalImage)