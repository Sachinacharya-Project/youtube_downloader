from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
from find_video import download, checkExistence, rename, comp as complete
import os
username = os.environ.get("USERPROFILE")
print("""
YouTube Video Downloader
Welcome to VERSION 0.0.2
Created by Sachin Acharya
""")
url = input("YouTube URL/Name: ")
asking = input("Audio(A) or Video(V): ").lower()
if asking != 'a' and asking != 'v':
    print('Wrong Format given. Downloading as VIDEO')
    asking = 'v'
if str(url).startswith('https://www.youtube.com'):
    if str(url).startswith('https://www.youtube.com/playlist'):
        ytd = Playlist(url)
        print("Total Contents: {}\n".format(len(ytd)))
        videoURLS = ytd.video_urls
        if asking == 'a':
            j=1
            ctx = ''
            for url in videoURLS:
                ctx = download(url, 'a', index=j)
                j=j+1
            print(ctx)
        else:
            j=1
            ctx = ''
            for url in videoURLS:
                ctx = download(url, 'v', index=j)
                j=j+1
            print(ctx)
    else:
        print(download(url, asking))
elif str(url) == '' or None:
    print('Empty String')
    exit()
else:
    if asking == 'a':
        print(download(url, 'a'))
    else:
        print(download(url, 'v'))