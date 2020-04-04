from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import MyUser


def generate_customer_profile(sender, instance, created, **kwargs):

    if not instance.is_staff:
        if created:

            group = Group.objects.get(name='FreemiumMember')
            instance.groups.add(group)
            username = instance.username

            MyUser.objects.create(user=instance, my_username=username)

            print("A user has been created (of type MyUser)")


post_save.connect(generate_customer_profile, sender=User)