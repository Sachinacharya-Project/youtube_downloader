from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
from find_video import download
import os
username = '.'
def complete():
    print(u'\u2713')
def checkExistence(file):
    data = os.path.join(username, 'Music')
    data = os.path.join(data, f'{file}.mp3')
    data = os.path.exists(data)
    return data
def rename(direc):
    direc = direc.replace('/', '\\')
    source = direc
    direc = direc.replace(".mp4", ".mp3")
    path = direc
    try:
        os.rename(source, path)
        complete()
    except FileExistsError:
        print("\nFile Already Exist")
checkExistence('Y2Mate.is - Harry Styles - Falling (Official Video)-olGSAVOkkTI-160k-1609919026713')
print("YouTube Video Downloader\nWelcome to VERSION 0.1.2\nCreated by Sachin Acharya\n")
asking = input("Wanna Download with URL(U) or Name(N)?: ").lower()
if asking == 'u':
    url = input("Url: ")
    asking = input("Playlist(P) or Single(S): ").lower()
    if asking == 'p':
        asking = input("Audio(A) or Video(V): ").lower()
        ytd = Playlist(url)
        print("Total Contents: {}\n".format(len(ytd)))
        if asking == 'a':
            j=1
            for audio in ytd.videos:
                title = audio.title
                if checkExistence(title) == True:
                    print("Audio Already Exist With Name {}.mp3".format(title))
                else:
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
        if url == '':
            print("Sorry, Cannot Process Empty String")
        else:
            asking = input("Audio(A) or Video(V): ").lower()
            ytd = YouTube(url, on_progress_callback=on_progress)
            if asking == 'a':
                title = ytd.title
                if checkExistence(title) == True:
                    print("Audio Already Exist with name {}.mp3".format(title))
                else:
                    print("Downloading Audio {}.mp3\n".format(title))
                    cb = ytd.streams.get_audio_only().download(f"{username}/Music")
                    ytd.register_on_complete_callback(rename(cb))
            elif asking == 'v':
                print("Downloading Video {}.mp4\n".format(ytd.title))
                ytd.streams.get_highest_resolution().download(f"{username}/Videos")
                ytd.register_on_complete_callback(complete())
            else:
                print("Wrong Command Given Downloading as Video")
                print("Downloading Video {}.mp4\n".format(ytd.title))
                ytd.streams.get_highest_resolution().download(f"{username}/Videos")
                ytd.register_on_complete_callback(complete())
    print(u"Download is Completed Successfully\n")
else:
    topic = input("Title of Video: ")
    asking = input("Audio(A) or Video(V): ").lower()
    if topic == '':
        print("Sorry, Cannot Process Empty String")
    else:
        if asking == 'a':
            download(topic, 'a')
        elif asking == 'v':
            download(topic, 'v')
        else:
            print("Wrong Key Pressed. Downloading as a Video")
            download(topic, 'v')
