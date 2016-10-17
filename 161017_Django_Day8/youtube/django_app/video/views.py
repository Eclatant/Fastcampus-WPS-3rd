from django.shortcuts import render
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


DEVELOPER_KEY = "AIzaSyDiarbwPOxSkXmNPfdv8UtHcZM6KySpk34"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword, page_token, max_results=10):
    """
    youtube_search함수 개선

    1. youtube_search 함수의 arguments에 pageToken 추가
    2. 받은 pageToken값을 youtube.search()실행 시 list의 인자로 추가
    3. search뷰에서 request.GET에 pageToken값을 받아오도록 설정
    4. template에서 이전페이지/다음페이지 a태그 href에 GET parameter가 추가되도록 설정
    """
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=max_results,
        pageToken=page_token
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
    context = {}
    keyword = request.GET.get('keyword')
    page_token = request.GET.get('page_token')
    if keyword:
        response = youtube_search(keyword)
        context['keyword'] = keyword
        context['response'] = response
    return render(request, 'video/search.html', context)
