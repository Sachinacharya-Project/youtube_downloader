from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
import os
username = os.environ.get("USERPROFILE")
def complete():
    print(u'\u2713')
def rename(direc):
    direc = direc.replace('/', '\\')
    source = direc
    direc = direc.replace(".mp4", ".mp3")
    path = direc
    os.rename(source, path)
asking = input("Playlist(P) or Single(S): ").lower()
if asking == 'p':
    url = input("Url: ")
    asking = input("Audio(A) or Video(V): ").lower()
    ytd = Playlist(url)
    print("Total Contents: {}\n".format(len(ytd)))
    if asking == 'a':
        j=1
        for audio in ytd.videos:
            title = audio.title
            print("{}: Audio {}.mp3 is downloading\n".format(j, title))
            try:
                audio.register_on_progress_callback(on_progress)
                cb = audio.streams.get_audio_only().download(f"{username}\\Music")
                audio.register_on_complete_callback(complete())
                rename(cb)
            except:
                print("{} cannot be downloaded\n".format(title))
                continue
            j=j+1
    else:
        print("Downloading Videos\n")
        i=1
        for video in ytd.videos:
            title = video.title
            print("{}: Video {}.mp4 is downloading\n".format(i, title))
            try:
                video.register_on_progress_callback(on_progress)
                video.streams.get_highest_resolution().download(f"{username}\\Videos")
                video.register_on_complete_callback(complete())
            except:
                print("{}.mp4 cannot be downloaded\n".format(title))
            i=i+1
else:
    url = input("Url: ")
    asking = input("Audio(A) or Video(V): ").lower()
    ytd = YouTube(url, on_progress_callback=on_progress)
    if asking == 'a':
        title = ytd.title
        print("Downloading Audio {}.mp3\n".format(title))
        cb = ytd.streams.get_audio_only().download(f"{username}/Music")
        ytd.register_on_complete_callback(rename(cb))
    else:
        print("Downloading Video {}.mp4\n".format(ytd.title))
        ytd.streams.get_highest_resolution().download(f"{username}/Videos")
print(u"Download is Completed Successful\n")