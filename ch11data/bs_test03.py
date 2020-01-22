# 라이버러리 읽어 들이기
from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver.com</li>
    <li><a href="http://www.daum.net">daum.com</li>
  </ul>
</body></html>
"""

# 데이터로 활용하기 위해서 저장할 리스트 선업
linklist = []

# HTML 분석하기
soup = BeautifulSoup(html, 'html.parser')

# a 태그의 데이터가 여러개 이므로
# find() 데이터 한개를 찾아옴  find_all() 전부다 찾아옴
# find_all() 메소드로 원하는 부분 추출하기
links = soup.find_all("a")
print(links)

# 링크목록 출력하기
for a in links:
    # 데이터 한개를 가져오면 딕셔너리로 저장 -> {site:값, url:값}
    data = {}
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)
    data["site"] = text
    data["url"] = href
    linklist.append(data)

print(linklist)
