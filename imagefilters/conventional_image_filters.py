from PIL import Image
import numpy as np
import cv2
from io import BytesIO

from django.core.files.base import ContentFile



def gaussian_image_filter(image_from_imageField, apply_filter_this_many_times=4):

    try:
        pil_image = Image.open(image_from_imageField)
    except:
        print("Error opening image")
        return
    else:
        np_image = np.asarray(pil_image)
        np_image = cv2.cvtColor(np_image, cv2.COLOR_RGBA2BGRA)

        kernel = np.ones((5, 5), np.float32) / 25

        dst = cv2.filter2D(np_image, -1, kernel)

        for i in range(apply_filter_this_many_times-1):
            dst = cv2.filter2D(dst, -1, kernel)


        dst = cv2.cvtColor(dst, cv2.COLOR_BGRA2RGBA)

        modified_pil_image = Image.fromarray(dst)
        img_io = BytesIO()
        modified_pil_image.save(img_io, format='PNG', quality=100)
        img_content = ContentFile(img_io.getvalue(), 'img.png')

        pil_image.close()

        return img_content


def edging_image_filter(image_from_imageField):

    try:
        pil_image = Image.open(image_from_imageField)
    except:
        print("Error opening image")
        return
    else:
        np_image = np.asarray(pil_image)
        np_image = cv2.cvtColor(np_image, cv2.COLOR_RGBA2BGRA)

        edges_image = cv2.Canny(np_image, 100, 100)

        modified_pil_image = Image.fromarray(edges_image)
        img_io = BytesIO()
        modified_pil_image.save(img_io, format='PNG', quality=100)
        img_content = ContentFile(img_io.getvalue(), 'img.png')

        pil_image.close()

        return img_content


def rgb_to_gray(image_from_imageField):

    try:
        pil_image = Image.open(image_from_imageField)
    except:
        print("Error opening image")
        return
    else:
        np_image = np.asarray(pil_image)
        np_image = cv2.cvtColor(np_image, cv2.COLOR_RGBA2GRAY)

        modified_pil_image = Image.fromarray(np_image)
        img_io = BytesIO()
        modified_pil_image.save(img_io, format='PNG', quality=100)
        img_content = ContentFile(img_io.getvalue(), 'img.png')

        pil_image.close()

        return img_content
