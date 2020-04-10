import youtube_dl
import logging
import ffmpeg
import argparse
import sys


logging.basicConfig(filename='error.log', format='%(filename)s: %(message)s',
                    level=logging.ERROR)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl' : 'YTDL_Downloaded//%(playlist)s//%(title)s.%(ext)s',       
    'noplaylist' : True,
    'continue_dl': False,
    'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            },
            {'key': 'FFmpegMetadata'},
        ],
}
async def download(link):
    with youtube_dl.YoutubeDL(ydl_opts) as ytdl:
        ytdl.download([link])

parser = argparse.ArgumentParser(description='Download songs from youtube, soundcloud etc.')
parser.add_argument("--url", help="Provide link to video/playlist",
                    type=download,
                    action="store")
if len(sys.argv)==1: # when url is not provided exit
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()
