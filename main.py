
def choose_file():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file = filedialog.askopenfilename(title='Choose File', filetypes=(('Plain Text', '*.txt'), ('List File', '*.lst')))
    return file
def downloader_(url, form='v'):
    from pytube import YouTube
    from pytube import Playlist
    from pytube.cli import on_progress
    from find_video import download, checkExistence, rename, comp as complete
    import os
    # username = os.environ.get("USERPROFILE")
    """
    Download Video: URL must be array or list of URIs
    """
    if 'list' not in str(type(url)):
        print("Only LIST of URI is Acceptible")
        exit(1)
    if form != 'a' and form != 'v':
        print('Wrong Format given. Downloading as VIDEO')
        form = 'v'
    count = 1
    for uri in url:
        print('On: {} / {}'.format(count, len(url)))
        count = count + 1
        if str(uri).startswith('https://www.youtube.com'):
            if str(uri).startswith('https://www.youtube.com/playlist'):
                ytd = Playlist(uri)
                print("Total Contents in PlayList: {}\n".format(len(ytd)))
                videoURLS = ytd.video_urls
                if form == 'a':
                    j=1
                    ctx = ''
                    for urll in videoURLS:
                        ctx = download(urll, 'a', index=j)
                        j=j+1
                    print(ctx)
                else:
                    j=1
                    ctx = ''
                    for urll in videoURLS:
                        ctx = download(urll, 'v', index=j)
                        j=j+1
                    print(ctx)
            else:
                print(download(uri, form))
        elif str(uri) == '' or None:
            print('Empty String')
            continue
        else:
            if form == 'a':
                print(download(uri, 'a'))
            else:
                print(download(uri, 'v'))
def print_menu():
    print("""Choose Menu
    1. Load from File
    2. Enter Manually
    3. Exit
    """)
if __name__ == '__main__':
    print("""Welcome
    YouTube Video Downloader
    Welcome to VERSION 1.0.0
    Created by Sachin Acharya
    """)
    print_menu()
    try:
        shit = int(input("Menu: "))
    except:
        print("Invalid Menu: Defaulting to Enter Manually")
        shit = 2
    url = []
    if shit == 1:
        print("Opening File Menu")
        file = open(choose_file(), 'r')
        lines = file.readlines()
        for urilist in lines:
            if not str(urilist).startswith("#"):
                url.append(str(urilist).replace('\n', ''))
    elif shit == 3:
        print('Thanks For Using Our Service')
        exit()
    else:
        while True:
            data = input("Enter URL/Name (quit() when done): ")
            if data.lower() == 'quit()':
                if len(url) == 0:
                    print("Need Atlease a URL")
                    if input("Enter Q to Close anyway else hit enter").lower() == 'q':
                        exit()
                else:
                    break
            else:
                url.append(data.replace("\n", ''))
    form = input("You wanna download as Audio(A) or Video(V): ").lower()
    downloader_(url, form)
    print("Completed Successfully")