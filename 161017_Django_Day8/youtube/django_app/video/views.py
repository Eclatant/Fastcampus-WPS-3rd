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


