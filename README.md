# 남서울대학교 사이버 강의 다운로더 (NSU Cyber Lecture Downloader)
Namseoul Univ. (NSU) Cyber Lecture Downloader (https://lms.nsu.ac.kr)  
위 프로그램을 사용하기 위해선 ffmpeg를 path에 등록해두거나 main.py 파일과 같은 경로에 ffmpeg.exe 파일을 위치시켜야 합니다.  
테스트 된 환경 : Windows 10 64bit

# Screenshot
![KakaoTalk_20200402_015025710](https://user-images.githubusercontent.com/10193967/78164242-6e1b2800-7484-11ea-98e7-68ce2d371a11.png)

# URL 형식
링크 형식은 다음과 같습니다.  
rtmp://nsu.vod.cdn.cloudn.co.kr/nsu/_definst_/nsucdn_nsu/lms_nsu/course_vod/강좌코드/강의코드/영상이름.mp4  
강좌코드의 경우 동일한 강좌라면 코드 또한 동일하며 (ex. A과목을 수강중이라면 1주차, 2주차, 3주차, ..., n주차 모두 강좌 코드는 동일합니다)  
강의코드의 경우 강좌나 회차수에 관계 없이 모두 동일한 것으로 추측이 됩니다.  
영상 재생 엔진으론 Wowza Streaming Engine 4를 사용하고 있습니다.  
사이트에서 스트리밍을 할 때는 Flash Player에서 rtmp 형식의 링크를 사용합니다만, 다운로드를 할 때 위의 프로토콜을 사용하면 강의 시간만큼 다운로드 시간이 비례하여 증가하게 됩니다.  
위의 문제를 해결하기 위하여 이 프로그램은 Wowza http 가속 다운로드 기능과 Intel Quicksync 기술을 사용합니다.
(약 24분 30초 영상을 다운로드 하는데 3분 30초 소요)  
프로그램을 실행한 뒤 입력창이 뜬다면 아래의 URL을 참고하여 값을 입력해주면 됩니다.     rtmp://nsu.vod.cdn.cloudn.co.kr/nsu/_definst_/nsucdn_nsu/lms_nsu/course_vod/과목코드/강의코드/영상이름.mp4  
(ex. URL이 rtmp://nsu.vod.cdn.cloudn.co.kr/nsu/_definst_/nsucdn_nsu/lms_nsu/course_vod/000000/000001/xxxx-xxxx-xxxx-xxxx.mp4라면 강좌코드엔 000000, 강의코드엔 000001, 영상이름엔 xxxx-xxxx-xxxx-xxxx (.mp4는 빼야합니다)를 입력해주면 됩니다.)  

# URL 확인 방법  
강의 영상을 재생한 뒤 크롬 기준 F12를 눌러 개발자 도구를 여세요.  
html 소스가 나왔다면 Ctrl + F 두 키를 눌러서 검색창을 연 뒤 rtmp이라고 검색해보세요.  
아래의 사진과 같은 화면이 나올 때까지 Enter를 눌러주시면 됩니다.
![SE-b9d93c8c-accc-4642-9aed-9df8d41906fe](https://user-images.githubusercontent.com/10193967/78167163-f7ccf480-7488-11ea-8aa4-020078f7ee02.png)  
위의 사진과 같은 내용이 나왔다면 Ctrl + C를 눌러서 내용물을 복사하고, Notepad와 같은 곳에 붙여넣어 주세요.  
그리고 rtmp 형식의 링크를 찾아서 따로 빼내어주면 URL 확인 작업이 끝납니다.
