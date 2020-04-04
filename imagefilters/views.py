from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Create your views here.
def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # TODO : add email as an authentication parameter in the line bellow
        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user=user)
            print('login was successful!')
            return redirect('/home')

    context = {}
    return render(request, 'imagefilters/login_page.html', context=context)


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

def user_profile(request):

    context = {}
    return render(request, 'imagefilters/user_profile_page.html', context=context)


def user_home_page(request):

    user = request.user
    username = user.username
    email = user.email

    context = {}
    return render(request, 'imagefilters/home_page.html')


