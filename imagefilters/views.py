from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from .decorators import unauthenticated_user
from .conventional_image_filters import *


# Create your views here.

@unauthenticated_user
def login_page(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"email is : {email}")
        print(f"password is : {password}")

        # TODO : add email as an authentication parameter in the line bellow
        user = authenticate(request, email=email, password=password)


        if user is not None:
            login(request, user=user)
            print('login was successful!')
            return redirect('/home')

    context = {}
    return render(request, 'imagefilters/login_page.html', context=context)

@unauthenticated_user
def register_page(request):

    create_user_form = CreateUserForm()

    if request.method == 'POST':

        create_user_form = CreateUserForm(request.POST)

        if create_user_form.is_valid():
            create_user_form.save()
            print("form has been saved!")
            return redirect('/login')

    context = {'create_user_form':create_user_form}
    return render(request, 'imagefilters/register_page.html', context=context)


def logout_user(request):

    logout(request)
    return redirect('/login')

@login_required
def user_profile(request):

    context = {}
    return render(request, 'imagefilters/user_profile_page.html', context=context)

@login_required
def update_user_profile(request):

    myuser = request.user.myuser

    form = MyUserForm(instance=myuser)

    if request.method == 'POST':

        form = MyUserForm(request.POST, instance=myuser)

        if form.is_valid():
            form.save()
            print("form has been saved (update_user_profile)")
            return redirect('/profile')

    context = {'form' : form}
    return render(request, 'imagefilters/update_user_profile_form.html', context=context)

@login_required
def user_home_page(request):

    user = request.user
    #image_url = user.myuser.useroriginalimage_set.get(pk=1).original_image.url
    images = user.myuser.useroriginalimage_set.all()

    context = {'images':images}
    return render(request, 'imagefilters/home_page.html', context=context)

@login_required
def upload_images(request):

    OriginalImageFormset = inlineformset_factory(MyUser, UserOriginalImage,
                                                 fields=('original_image_name', 'original_image'), extra=1)

    formset = OriginalImageFormset(queryset=UserOriginalImage.objects.none(), instance=request.user.myuser)

    if request.method == 'POST':

        formset = OriginalImageFormset(request.POST, request.FILES, instance=request.user.myuser)

        if formset.is_valid():
            formset.save()
            print('upload image form has been saved')

            return redirect('/home')
        else:
            print('upload_imgs_form.errors : ', formset.errors)

    context ={'upload_imgs_formset':formset}
    return render(request, 'imagefilters/upload_images_form.html', context=context)

@login_required
def image_filtering_options(request, pk):

    original_img = request.user.myuser.useroriginalimage_set.get(pk=pk).original_image
    all_filtered_imgs = [img.edited_image for img in request.user.myuser.useroriginalimage_set.get(pk=pk).usereditedimage_set.all()]

    context = {'original_img':original_img, 'all_filtered_imgs':all_filtered_imgs, 'pk_original_img':pk}
    return render(request, 'imagefilters/image_filtering_options.html', context=context)

@login_required
def filter_image_form(request, pk):

    EditedImageFormSet = inlineformset_factory(UserOriginalImage, UserEditedImage, fields=('filter_type',), extra=1)

    my_instance = UserOriginalImage.objects.get(pk=pk)
    formset = EditedImageFormSet(queryset=UserEditedImage.objects.none(), instance=my_instance)

    #form = EditImagesForm()

    if(request.method == 'POST'):

        #form = EditImagesForm(request.POST)
        formset = EditedImageFormSet(request.POST, instance=my_instance)

        if formset.is_valid():
            formset.save()

            print('form.cleaned_data = ', formset.cleaned_data)

            return redirect('/home')

    context ={'formset':formset}
    return render(request, 'imagefilters/filter_image_form.html', context=context)

@login_required
def apply_gaussian_filter(request, pk):

    original_img = UserOriginalImage.objects.get(pk=pk)
    original_img.gaussian_filter()

    return redirect('/home/filtering_options/{}'.format(pk))

@login_required
def apply_edging_filter(request, pk):

    original_img = UserOriginalImage.objects.get(pk=pk)
    original_img.edging_filter()

    return redirect('/home/filtering_options/{}'.format(pk))

@login_required
def apply_rgb2gray_filter(request, pk):

    original_img = UserOriginalImage.objects.get(pk=pk)
    original_img.rgb2gray_filter()

    return redirect('/home/filtering_options/{}'.format(pk))