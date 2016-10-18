from django.shortcuts import render
from django.http import HttpResponse
from video.models import Video
__all__ = ['bookmark_add', 'bookmark_list']


def bookmark_add(request):
    try:
        kind = request.POST['kind']
        video_id = request.POST['video_id']
        title = request.POST['title']
        description = request.POST['description']
        published_date = request.POST['published_date']
        thumbnail_url = request.POST['thumbnail_url']

        Video.objects.create(
            kind=kind,
            youtube_id=video_id,
            title=title,
            description=description,
            published_date=published_date,
            thumbnail=thumbnail_url
        )
        return HttpResponse('Success')
    except Exception as e:
        return HttpResponse('Exception! %s (%s)' % (e, e.args))


def bookmark_list(request):
    """
    추가한 Video인스턴스 목록을 보여주는 페이지
    """
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'video/bookmark_list.html', context)