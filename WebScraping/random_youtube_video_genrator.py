from googleapiclient.discovery import build
import random
import webbrowser

DEVELOPER_KEY = 'AIzaSyCv-IIGcdyrQVRNEXvuNLtRxlBULLAmgQQ'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

prefix = ['IMG ', 'IMG_', 'IMG-', 'DSC ']
postfix = [' MOV', '.MOV', ' .MOV']

def youtube_search():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=random.choice(prefix) + str(random.randint(25, 30)) + random.choice(postfix),
    part='snippet',
    maxResults=5
  ).execute()

  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s' % (search_result['id']['videoId']))
  video_id = videos[random.randint(0, 2)]

  webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")



youtube_search()