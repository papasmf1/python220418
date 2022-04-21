# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) / 사람인척 하는 것
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("c:\\work\\land.txt", "wt", encoding="utf-8")
for n in range(1,10):
        #클리앙의 중고장터 주소  ### change
        # data ='https://price.joinsland.joins.com/theme/index_theme.asp?CSRFToken=QTBXHIeBclsWuqhLwvMtGyPvQJwMBKgRjVsBUjsP&sisaegbn=T07&areaCode=4141000000&searchgbn=&page=' + str(n)
        data ='https://price.joinsland.joins.com/theme/index_theme.asp?CSRFToken=QoirJNvBMKgtFgSKqmIjdNVhwHBjlNkdeoiuTPvs&sisaegbn=T07&areaCode=4111700000&searchgbn=&page=' + str(n)
        print (data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore') # 한글을 올바르게 해석, 잘못될경우 빼주면 된다.
        soup = BeautifulSoup(page, 'html.parser')

        # <td class="txt_addres2">당동</td>
        # <td class="txt_danzi"><a href="/area/?mcateGroup=A1&areaCode=4141010100&danjiId=15287">용호마을e-편한세상</a></td>
        # <td class="num_area"><a href="/area/?mcateGroup=A1&areaCode=4141010100&danjiId=15287&ptype=3">151A</a></td>
        # <td class="num_year">2005</td>
        # <td class="num_household">1,247</td>
						
                        # <tr>
						# 	<td class="num_ranking">2</td>
						# 	<td class="txt_addres2">당동</td>
						# 	<td class="txt_danzi"><a href="/area/?mcateGroup=A1&areaCode=4141010100&danjiId=15287">용호마을e-편한세상</a></td> # 2
						# 	<td class="num_area"><a href="/area/?mcateGroup=A1&areaCode=4141010100&danjiId=15287&ptype=2">109</a></td> # 3
						# 	<td class="num_year">2005</td> # 4n
						# 	<td class="num_household">1,247</td> # 5n
							
						# 	<td class="num_per">2.59%</td> # 6n
							
						# 	<td class="num_price">44,500 ~ 52,500</td> # 7n
						# 	<td class="num_maemul"><a href="http://maemul.joinsland.joins.com/maemul/?mcateGroup=A1|A3|A4&amp;sale_type=1&amp;areaCode=4141010100&amp;danjiId=15287" target="_blank">1</a></td> #8
						# 	<td class="num_price">40,000 ~ 44,000</td> # 9n
						# 	<td class="num_maemul"><a href="http://maemul.joinsland.joins.com/maemul/?mcateGroup=A1|A3|A4&&amp;sale_type=2&amp;areaCode=4141010100&amp;danjiId=15287" target="_blank">0</a></td>
						# </tr>

        list = soup.find_all('td', attrs={'class':'txt_danzi'})

        for item in list:
                try:
                        item2 = item.find("a").text 
                        #print(item2)
                        item3 = item.find_next("td")
                        #print(item3.find("a").text)
                        item4 = item3.find_next("td")
                        #print(item3.text)
                        item5 = item4.find_next("td")
                        #print(item2)
                        item6 = item5.find_next("td")
                        #print(item3.find("a").text)
                        item7 = item6.find_next("td")
                        #print(item2)
                        price1 = item7.text.split() 
                        item8 = item7.find_next("td")
                        price2 = item8.text.split() 
                        totalPrice = int(price1[0].replace(",","")) - int(price2[0].replace(",",""))

                        #print(item3.find("a").text)
                        item9 = item8.find_next("td")
                        
                        #print(item3.text)
                        print("{0} , {1} , {2}, {3}, {4}, {5}, {6}".format(item2, item3.find("a").text, item4.text, item5.text, item6.text, item7.text, totalPrice))
                        f.write("{0} , {1} , {2}, {3}, {4}, {5}, {6}".format(item2, 
                                item3.find("a").text, item4.text, item5.text, item6.text, 
                                item7.text, totalPrice) + "\n")
                        
                ### 에러가 날 경우, 빠져 나오라는 예외 처리
                except:
                        pass
        
f.close() 