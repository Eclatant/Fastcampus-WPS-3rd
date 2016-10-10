from django.shortcuts import render, HttpResponse
from .models import Post

# 같은 의미
# from blog.models import Post


def post_list(request):
    return render(request, 'blog/post_list.html', {})
