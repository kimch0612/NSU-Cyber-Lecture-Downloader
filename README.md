# 남서울대학교 사이버 강의 다운로더 (NSU Cyber Lecture Downloader)
Namseoul Univ. (NSU) Cyber Lecture Downloader (https://lms.nsu.ac.kr)  
위 프로그램을 사용하기 위해선 ffmpeg를 path에 등록해두거나 main.py 파일과 같은 경로에 ffmpeg.exe 파일을 위치시켜야 합니다.  
Windows 10 환경에서만 사용 가능합니다.

**Screenshot**
![KakaoTalk_20200402_015025710](https://user-images.githubusercontent.com/10193967/78164242-6e1b2800-7484-11ea-98e7-68ce2d371a11.png)

**URL 형식**  
rtmp://nsu.vod.cdn.cloudn.co.kr/nsu/_definst_/nsucdn_nsu/lms_nsu/course_vod/과목코드/강의코드/영상이름.mp4  
영상 재생 엔진으론 Wowza Streaming Engine 4를 사용합니다.  
위 프로그램은 Wowza http 가속 다운로드 기능을 사용하므로 rtmp 링크 형식이 아니라 http 링크 형식을 사용해야 합니다.
