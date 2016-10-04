from django.shortcuts import render, render_to_response
from .models import Post


# post_list라는 이름의 view
# Post인스턴스를 전부 가져와 posts라는 이름으로 'post_list.html'템플릿에 전달해준다
def post_list(request):
    posts = Post.objects.all()
    ret = {
        'posts': posts
    }
    return render_to_response('post_list.html', ret)