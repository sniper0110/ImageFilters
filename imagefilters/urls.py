from django.urls import path
from . import views


app_name='imagefilters'

urlpatterns=[
    path('login', views.login_page, name='loginPage'),
    path('register', views.register_page, name='registerPage'),
    path('home', views.user_home_page, name='home_page'),
    path('', views.logout_user, name='logout_user'),

    path('profile', views.user_profile, name='user_profile'),
    path('profile/update', views.update_user_profile, name='update_user_profile'),

    path('home/upload_images', views.upload_images, name='upload_imgs'),
    path('home/filtering_options/<str:pk>', views.image_filtering_options, name='filtering_options'),
    path('home/filtering_options/<str:pk>/filtering_form', views.filter_image_form, name='filter_image_form'),

    path('home/filtering_options/<str:pk>/blurring', views.apply_gaussian_filter, name='gaussian_filter'),
    path('home/filtering_options/<str:pk>/edging', views.apply_edging_filter, name='edging_filter'),
    path('home/filtering_options/<str:pk>/blackAndWhite', views.apply_rgb2gray_filter, name='rgb2gray_filter'),
]