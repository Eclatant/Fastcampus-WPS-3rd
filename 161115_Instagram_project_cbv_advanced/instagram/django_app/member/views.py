from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import LoginForm


def login_fbv(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
    else:
        form = LoginForm()
        
    context = {
        'form': form,
    }
    return render(request, 'member/login.html', context)