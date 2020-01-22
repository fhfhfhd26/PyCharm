# 1. 214.png 파일을 test.png로 다운로드하기
# 라이브러리 읽어 들이기
import urllib.request

# URL과 저장경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드
urllib.request.urlretrieve(url, savename)
print("저장완료")

# 파일 오픈하는 형식에 의해서 데이터를 읽어서 저장하는 방식으로 처리
savename = "test1.png"

# 파일 오픈하는 형식에 의해서 데이터를 읽어서 저장하는 방식으로처리
# 이미지 데이터 읽어오기
mem = urllib.request.urlopen(url).read()

# with 문으로 선언되 객체는 with문 밖으로 나가면서 close()된다
# java --> try(자원선언) try 문 밖으로 나가면서 close()된다.
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장완료2")

# 2. 다운로드 받고자하는 이미지 파일을 찾아서 다운로드하기
# URL과 저장경로 지정하기
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6t1PwuwtxGitoPslRthtzSM7QpnIEPnEUZH78aFzekiquQ5qjJg&s"
savename = "cat.png"

# 다운로드
urllib.request.urlretrieve(url, savename)
print("저장완료3")
