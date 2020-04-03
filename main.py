import subprocess

gangjoa = []
gangyee = []
name = []

down = input("다운로드 받을 영상의 총 개수를 입력하여 주세요 (예: 3) : ")
for a in range(0), range(down):
    gangjoa.append(input("%s번째로 다운 받을 강좌의 강좌 코드를 입력해 주세요 : ") & (a))
    gangyee.append(input("%s번째로 다운 받을 강좌의 강의 코드를 입력해 주세요 : ") & (a))
    name.append(input("%s번째로 다운 받을 강좌의 영상 이름을 입력해 주세요 : ") & (a))
    a += 1
for i in range(0), range(down):
    subprocess.call ('ffmpeg -i http://nsu.vod.cdn.cloudn.co.kr/nsu/_definst_/nsucdn_nsu/lms_nsu/course_vod/%s/%s/%s.mp4/playlist.m3u8 -acodec copy -absf aac_adtstoasc %s.mp4'% (gangjoa[i], gangyee[i], name[i]), shell=True)
    i += 1