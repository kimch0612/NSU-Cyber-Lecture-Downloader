import subprocess
import os

name = []
file = []

down = input("다운로드 받을 영상의 총 개수를 입력하여 주세요 (예: 3) : ")
down1 = int(down)
gangjoa = input("다운로드할 강좌의 '강좌 코드'를 입력해 주세요 (5자리 숫자로 구성 됨) : ")
gangyee = input("다운로드할 강좌의 '강의 코드'를 입력해 주세요 (5자리 숫자로 구성 됨) : ")

for a in range(1, down1+1):
    print("%s번째로 다운로드할 강좌의 '영상 이름'을 입력해 주세요" % (a))
    g1 = input("입력 예시 : xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.mp4 : ")
    name.append(g1)
    g2 = input("%s번째로 다운로드할 강좌의 파일 이름을 입력해 주세요 (예 : 1st) : " % (a))
    file.append(g2)
    a += 1

try:
    os.mkdir("%s" % (gangjoa))
except:
    pass

os.chdir(gangjoa)

for i in range(0, down1):
    subprocess.call ('ffmpeg -i http://nsu.vod.cdn.cloudn.co.kr/nsu/_definst_/nsucdn_nsu/lms_nsu/course_vod/%s/%s/%s/playlist.m3u8 -preset veryfast -acodec copy -b:v 6000k %s.mp4'% (gangjoa, gangyee, name[i], file[i]), shell=True)
    i += 1

print("Done!")