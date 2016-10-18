__all__ = ['add_bookmark', 'bookmark_list']

def add_bookmark(request):
    """
    POST요청을 받음

    kind
    videoId
    title
    description
    publishedAt
    thumbnails

    요소들을 사용해서​
        Video 인스턴스 생성 후
        받았던 페이지로 돌아가기
        request.path값을 POST안에 받아서 돌아와야 됨
    """
    pass


def bookmark_list(request):
    """
    추가한 Video인스턴스 목록을 보여주는 페이지
    """
    pass