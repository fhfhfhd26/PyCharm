# 라이버러리 읽어 들이기
from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
  <h1>스크레이핑이란?</h1>
  <p>웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

# HTML 분석하기
# 분석하고자 하는 HTML 데이터를 BrautifulSoup 파라메터로 넘김
soup = BeautifulSoup(html, 'html.parser')

# 원하는 부분 추출하기
h1 = soup.h1
h2 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# 요소의 글자 출력하기
print("h1(구조) = " + h1.string)
print("h2(단독) = " + h2.string)
print("p = " + p1.string)
print("p = " + p2.string)
