from django.shortcuts import render, render_to_response
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    ret = {
        'posts': posts
    }
    return render_to_response('post_list.html', ret)