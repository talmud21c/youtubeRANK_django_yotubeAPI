from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey = 'AIzaSyBKoeIuE-YBM1NYDIEv4chJrRtt_yGq4ic')


def get_youtube_channel_search_list(keyword):
    page_token = ''
    while (True):
        search_response = youtube.search().list(
            q = keyword,
            part = 'snippet',
            maxResults = 50,
            pageToken = page_token
        ).execute()
        for item in search_response['items']:
             channel_list.append(item['snippet']['channelId'])
        if ('nextPageToken' in search_response):
            page_token = search_response['nextPageToken']
        else:
            break