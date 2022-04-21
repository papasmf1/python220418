# web2.py 
#웹서버와 통신
import urllib.request
#웹크롤링
from bs4 import BeautifulSoup
#웹서버에 요청
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체
soup = BeautifulSoup(data, "html.parser")

# <td class="title">
# 	<a href="/webtoon/detail?titleId=20853">마음의 소리 50화 <격렬한 나의 하루> </a>
# </td>
cartoons = soup.find_all("td", class_="title")
print("개수:{0}".format(len(cartoons)))
#내부에 있는 <a>태그 검색 
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)

for item in cartoons:
    title = item.find("a").text 
    print(title.strip())



https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=1