import subprocess

a = input()
b = input()
subprocess.call ('ffmpeg -i http://%s/playlist.m3u8 -acodec copy -absf aac_adtstoasc %s.mp4'% (a, b), shell=True)