from django.shortcuts import render
from video.models import Video
__all__ = ['add_bookmark', 'bookmark_list']


def add_bookmark(request):
    """
    POST요청을 받음

    kind
    videoId
    title
    description
    publishedAt
    thumbnail

    요소들을 사용해서​
        Video 인스턴스 생성 후
        받았던 페이지로 돌아가기
        request.path값을 POST안에 받아서 돌아와야 됨
    """
    kind = request.POST['kind']
    video_id = request.POST['video_id']
    title = request.POST['title']
    description = request.POST['description']
    published_date = request.POST['published_date']
    thumbnail_url = request.POST['thumbnail_url']



def bookmark_list(request):
    """
    추가한 Video인스턴스 목록을 보여주는 페이지
    """
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'video/bookmark_list.html', context)