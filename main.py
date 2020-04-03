import subprocess

gangjoa = []
gangyee = []
name = []
file = []
i = 0

down = input("다운로드 받을 영상의 총 개수를 입력하여 주세요 (예: 3) : ")
down1 = int(down)

for a in range(1, down1+1):
    g1 = input("%s번째로 다운로드할 강좌의 '강좌 코드'를 입력해 주세요 : " % (a))
    gangjoa.append(g1)
    g2 = input("%s번째로 다운로드할 강좌의 '강의 코드'를 입력해 주세요 : " % (a))
    gangyee.append(g2)
    g3 = input("%s번째로 다운로드할 강좌의 '영상 이름'을 입력해 주세요 : " % (a))
    name.append(g3)
    g4 = input("%s번째로 다운로드할 강좌의 파일 이름을 입력해 주세요 : " % (a))
    file.append(g4)
    a += 1

for i in range(0, down1):
    subprocess.call ('ffmpeg -i http://nsu.vod.cdn.cloudn.co.kr/nsu/_definst_/nsucdn_nsu/lms_nsu/course_vod/%s/%s/%s.mp4/playlist.m3u8 -acodec copy -absf aac_adtstoasc %s.mp4'% (gangjoa[i], gangyee[i], name[i], file[i]), shell=True)
    i += 1

print("Done!")