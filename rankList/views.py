from pickle import GET

from django.shortcuts import render
from googleapiclient.discovery import build
import requests

from youtubeRANK import settings


def index(request):
    url = 'https://www.googleapis.com/youtube/v3/channels'
    params = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet',
        'type': 'video',
        'maxResults': '10',
    }

    response = request.get(url, params)
    response_dict = response.json()

    context = {
        'youtube_items': response_dict['items']
    }

    return render(request, 'rankList/index.html')