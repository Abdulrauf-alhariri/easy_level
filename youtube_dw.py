from pytube import YouTube
import urllib.request
from pathlib import Path
import os


def directory():
    path = Path(path)
    path.mkdir()


def high_quality(yt, path):
    return yt.streams[0].download(path)


def download():
    path = Path(path)
    try:
        yt = YouTube(input("Enter the link: "))
        if True:
            quality = input(
                "Do you want to download the highst qualtiy?(yes/ no)").lower()
            print("")

            if quality == "yes":
                try:
                    if True:
                        high_quality(yt, path)
                        print("Download is completed")

                except Exception as error:
                    print(error)

            elif quality == "no":
                for i in yt.streams.filter(progressive=True):
                    print(i)
                try:
                    stream_itag = int(input("Enter the stream itag: "))
                    if True:
                        yt.streams.get_by_itag(stream_itag).download(path)
                        print("Download is completed")

                except ValueError as v:
                    print(v)

            else:
                print("I don't understand, please write correctly")

    except:
        print("Check if the link is correct!")


download()
