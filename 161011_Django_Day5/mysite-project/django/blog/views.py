from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from .models import Post

# 같은 의미
# from blog.models import Post


def post_list(request):
    # posts = Post.objects\
    #     # .filter(published_date__lte=timezone.now())\
    #     .order_by('published_date')

    # published_date의 값이 데이터베이스에서 NULL일 경우
    posts = Post.objects \
        .filter(
            Q(published_date__lte=timezone.now()) |
            Q(published_date=None)
        ).order_by('published_date')
    return render(request, 'blog/post_list.html', {'post_list': posts, 'title': '타이틀 변수는 title키를 이용해서 접근'})


def post_detail(request, pk):
    """
    post_detail뷰(지금 작업중인 뷰)에서 전달받은 pk를 이용해서
    pk값(id값)이 전달받은 pk인 Post객체를 Query하여 post라는 변수에 할당
    해당 변수를 render함수를 이용, post_detail.html템플릿을 이용해 리턴 (post변수는 'post'키로 전달되도록 한다)
    """
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)
