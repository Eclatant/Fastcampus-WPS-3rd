from django.shortcuts import render
from .forms import LoginForm


def login_fbv(request):
    context = {
        'form': LoginForm(),
    }
    return render(request, 'member/login.html', context)