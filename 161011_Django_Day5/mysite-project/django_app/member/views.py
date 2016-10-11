from django.shortcuts import render
from django.contrib.auth import \
    authenticate as auth_authenticate, \
    login as auth_login
# https://docs.djangoproject.com/en/1.10/
# topics/auth/default/#auth-web-requests

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth_authenticate(
        username=username,
        password=password
    )

    if user is not None:
        auth_login(request, user)
        pass
    else:
        pass