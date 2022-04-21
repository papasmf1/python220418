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

