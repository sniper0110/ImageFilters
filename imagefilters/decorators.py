from django.shortcuts import redirect
from django.http import HttpResponse


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            print('user is authenticated inside decorator!')
            return redirect('/home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func