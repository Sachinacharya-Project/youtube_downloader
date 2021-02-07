"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by Sachin Acharya
This Piece of Code is Copied from My Previous Project 
(YouTube-Downloader-2) that is before updating this one. 
In this version I am Merging Both of my Project.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from pytube import YouTube
import os
import requests
from pytube.cli import on_progress

username = os.environ.get("USERPROFILE")

def comp():
    print(u'\u2713')
def play(topic):
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count-5] == "/results":
        raise Exception("No Video Found with that name")
    return "https://www.youtube.com"+lst[count-5]
def rename(direc):
    direc = direc.replace('/', '\\')
    source = direc
    direc = direc.replace(".mp4", ".mp3")
    path = direc
    try:
        os.rename(source, path)
    except FileExistsError:
        print("\nFile Already Exist")
    comp()
def download(topic, asking):
    url = play(topic)
    ytd = YouTube(url, on_progress_callback=on_progress)
    if asking == 'a':
        title = ytd.title
        if os.path.exists(os.path.join(os.path.join(username, 'Music'), f"{title}.mp3")):
            print("Audio Already Exist with Name {}.mp3".format(title))
        else:
            print("Downloading Audio {}.mp3".format(title))
            try:
                cb = ytd.streams.get_audio_only().download(f"{username}/Music")
            except ConnectionResetError:
                print("Audio cannot be downloaded=> Connection has been reset")
            ytd.register_on_complete_callback(rename(cb))
    elif asking == 'v':
        print("Downloading Video {}.mp4".format(ytd.title))
        try:
            ytd.streams.get_highest_resolution().download(f"{username}/Videos")
            ytd.register_on_complete_callback(comp())
        except ConnectionResetError:
            print("Video cannot be downloaded=>Connection reset")
    else:
        print("Invalid Argument")
    print("Download is Completed Successfully")