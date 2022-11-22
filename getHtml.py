import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME="youtube"
YOUTUBE_API_VERSION="v3"
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)



def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        pass

def extract_url(song):
    search_response = youtube.search().list(
        q = song,
        order = "viewCount",
        #order = "relevance",
        part = "snippet",
        maxResults = 1
                                  ).execute()

    # id = []
    # view = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            id = "%s" % (search_result["id"]["videoId"])
            # request = youtube.videos().list(part='statistics', id=search_result["id"]["videoId"])
            # response = request.execute()
            # view.append(response['items'][0]['statistics']['viewCount'])
                    
    # max_view = max(view)
    # max_view_idx = view.index(max_view)

    
    return id

def get_MV(id, song):
    html_text = f"""
        <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <iframe
                id="ytplayer"
                type="text/html"
                width="1440"
                height="810"
                src="https://www.youtube.com/embed/{id}"
                frameborder="0"
                allowfullscreen="allowfullscreen"></iframe>
        </body>
    </html>
    """
    html = "html/" + song + ".html"
    html_file = open(html, 'w')
    html_file.write(html_text)
    html_file.close()
    print(song, "success html")


