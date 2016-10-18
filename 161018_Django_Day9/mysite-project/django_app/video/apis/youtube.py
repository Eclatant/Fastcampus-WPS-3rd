from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from video.models import Video


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

    # video.search 뷰에서
    # search_response의 items를 반복하며
    # 반복하고있는 item의 'videoId'값이 이미 갖고있는 Video인스턴스의 youtube_id에 해당하는지 파악
    # 이미 Video인스턴스에 존재하는 video_id일 경우, is_exist에 True대입
    for item in search_response['items']:
        cur_video_id = item['id']['videoId']
        if Video.objects.filter(youtube_id=cur_video_id).exists():
           item['is_exist'] = True

    #
    video_id_list = [item['id']['videoId'] for item in search_response['items']]
    exist_list = Video.objects.filter(youtube_id__in=video_id_list)
    exist_id_list = [video.youtube_id for video in exist_list]
    for item in search_response['items']:
        cur_video_id = item['id']['videoId']
        if cur_video_id in exist_id_list:
            item['is_exist'] = True

    return search_response
