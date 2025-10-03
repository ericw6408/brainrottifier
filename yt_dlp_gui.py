import pygame
import os 
import sys
import shapes
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
import json 

# misc init vars

directory = os.path.abspath(os.getcwd())

# pygame vars

select_loop = True

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

colours = {
    "BACKGROUND": (149, 201, 181),
    "LIGHTBLUE":(149, 201, 201),
    "CAMBRIDGEBLUE":(149, 201, 181),
    "DAVYSGRAY":(77, 80, 97),
    "GLAUCOUS":(105, 128, 188),
    "SKYMAGENTA":(105, 128, 188)
}


# downloading to current directory, with the title and proper extension as the filename

ydl_opts = {
    "outtmpl": directory + "\\%(title)s.%(ext)s",
    "ignorerrors":True,
    "no_warnings":True,
    "noprogress":True,
    "quiet":True
}

Downloader = YoutubeDL(ydl_opts)

def download_MP4(urls:list[str])-> str:
    # function to download an mp4 file at the current directory given a valid url

    bad_URLS = []
    out_message = ""

    # checking for errors 

    for url in urls:
        try:
            vid_info = Downloader.extract_info(url,download=False)
            if vid_info:
                Downloader.download([url])
            else:
                bad_URLS.append(url)

        except DownloadError:
            bad_URLS.append(url)
    
    if bad_URLS != []:
        for url in bad_URLS:
            out_message += f"Invalid link: {url}"
    
    else:
        out_message = "All videos downloaded successfully to " + directory

    return out_message


def input_loop():

    while select_loop:
        clock.tick(144)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
        


Downloader.__exit__(None,None,None)



    