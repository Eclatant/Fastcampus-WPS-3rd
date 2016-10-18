from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from video.models import Video
__all__ = ['bookmark_add', 'bookmark_list']


def bookmark_add(request):
    path = request.POST.get('path')
    try:
        kind = request.POST['kind']
        video_id = request.POST['video_id']
        title = request.POST['title']
        description = request.POST['description']
        published_date = request.POST['published_date']
        thumbnail_url = request.POST['thumbnail_url']

        video = Video.objects.create(
            kind=kind,
            youtube_id=video_id,
            title=title,
            description=description,
            published_date=published_date,
            thumbnail=thumbnail_url
        )
        msg = '%s 영상을 북마크에 등록했습니다' % (
            video.title
        )
    except Exception as e:
        msg = 'Exception! %s (%s)' % (e, e.args)

    messages.success(request, msg)
    if path:
        return redirect(path)
    else:
        return redirect('video:bookmark_list')


def bookmark_list(request):
    """
    추가한 Video인스턴스 목록을 보여주는 페이지
    """
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'video/bookmark_list.html', context)