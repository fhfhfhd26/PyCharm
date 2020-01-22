# 라이버러리 읽어 들이기
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# urlopen()으로 데이터 가져오기
res = req.urlopen(url)

# BeautifulSoup로 분석하기
soup = BeautifulSoup(res, 'html.parser')

# 원하는 데이터 추출하기
title = soup.find('title').string
city = soup.find_all('city')
tmef = soup.find_all('tmef')
wf = soup.find_all('wf')
tmn = soup.find_all('tmn')
tmx = soup.find_all('tmx')

print(title)
print(soup)
for i in range(0, len(city)):
    print("--------------%s-------------" % city[i].string)

    for j in range(0, 13):
        print("일시 : ", tmef[(i*13)+j].string)
        print("날씨 : ", wf[(i*13)+j + 1].string)
        print("최저기온 : ", tmn[(i*13)+j].string)
        print("최고기온 : ", tmx[(i*13)+j].string)
