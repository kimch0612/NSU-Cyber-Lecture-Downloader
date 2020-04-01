# 남서울대학교 사이버 강의 다운로더 (NSU Cyber Lecture Downloader)
Namseoul Univ. (NSU) Cyber Lecture Downloader (https://lms.nsu.ac.kr)  
위 프로그램을 사용하기 위해선 ffmpeg를 path에 등록해두거나 main.py 파일과 같은 경로에 ffmpeg.exe 파일을 위치시켜야 합니다.  
Windows 10 환경에서만 사용 가능합니다.

**Screenshot**
![KakaoTalk_20200402_015025710](https://user-images.githubusercontent.com/10193967/78164242-6e1b2800-7484-11ea-98e7-68ce2d371a11.png)

**URL 형식**  
rtmp://nsu.vod.cdn.cloudn.co.kr/nsu/_definst_/nsucdn_nsu/lms_nsu/course_vod/과목코드/강의코드/영상이름.mp4  
영상 재생 엔진으론 Wowza Streaming Engine 4를 사용합니다.  
사이트에서 스트리밍을 할 때는 rtmp 형식의 링크를 사용합니다만, 다운로드를 할 때 위의 프로토콜을 사용하면 강의 시간만큼 다운로드 시간이 비례하여 증가하게 됩니다.  
위의 문제를 해결하기 위하여 이 프로그램은 Wowza http 가속 다운로드 기능을 사용하므로 rtmp 링크 형식이 아니라 http 링크 형식을 사용해야 합니다.  
프로그램을 실행한 뒤 URL 입력창이 뜬다면 rtmp://nsu.vod.cdn.cloudn.co.kr/nsu/_definst_/nsucdn_nsu/lms_nsu/course_vod/과목코드/강의코드/영상이름.mp4 이 아니라 http://nsu.vod.cdn.cloudn.co.kr/nsu/_definst_/nsucdn_nsu/lms_nsu/course_vod/과목코드/강의코드/영상이름.mp4 로 입력해주면 됩니다.  
