import os

def build_upload_to_path_for_original_image(instance, filename):
    return f"original_images/{instance.myuser.my_username}/{filename}"


def build_upload_to_path_for_edited_image(instance, filename):
    return f"edited_images/{instance.original_image.myuser.my_username}/{filename}"