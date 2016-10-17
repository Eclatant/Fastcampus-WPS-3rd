from django.shortcuts import render
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


DEVELOPER_KEY = "AIzaSyDiarbwPOxSkXmNPfdv8UtHcZM6KySpk34"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword, max_results=10):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=max_results
    ).execute()

    return search_response

import json
def search(request):
    # Template : 'video/search.html'
    # URL : 'video/search/'
    # view : search
    # Static, Templates 디렉토리 설정
    """
    1. STATICFILES_DIRS 설정
    2. templates폴더 생성 후 TEMPLATE의 DIRS안에 설정
    3. video/search.html파일 생성
    4. search.html내부 내용
        input
        ul > li (img, p*3)
    5. urls.py에 view연결
    6. view에서 video/search.html파일 render
    """
    # GET paramter에서 keyword값을 가져옵니다
    keyword = request.GET.get('keyword')
    response = youtube_search(keyword)
    print(json.dumps(response, indent=2, sort_keys=True))

    context = {
        'response': response,
    }
    return render(request, 'video/search.html', context)
