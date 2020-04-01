import subprocess

url = input("RTMP 형식의 URL을 입력하여 주세요 : ")
name = input("저장할 이름을 입력해 주세요 : ")
subprocess.call ('ffmpeg -i http://%s/playlist.m3u8 -acodec copy -absf aac_adtstoasc %s.mp4'% (url, name), shell=True)