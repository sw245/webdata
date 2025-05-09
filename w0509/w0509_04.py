import requests
from bs4 import BeautifulSoup


# url = 'https://finance.naver.com/sise/sise_market_sum.naver'
url = 'https://n.news.naver.com/article/011/0004483132?ntype=RANKING'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)

res.raise_for_status()
# print(res.text)     # 문자열

# 문자열 >> html, css 파싱
soup = BeautifulSoup(res.text,'lxml')
# print(soup)           # html, css

# print(soup.title)       # <title> 태그에 접근해서 가져옴
# print(soup.title.get_text())
# print(soup.header.div)
# print(soup.header.div.a)        # html 태그는 . 뒤로 붙이면 됨
# print(soup.header.div.a.attrs)  # html 태그의 속성을 모두 출력
# print(soup.header.div.a['href'])  # html 태그의 속성을 선택, 하나만 출력
# print(soup.header.div.a['class']) 

## 어떤 태그의 id,class 속성 출력
# find() 태그에서 검색할 때 사용

data1 = soup.find('a',attrs={'class':'ofhd_float_back _BACK'})  # 태그의 속성으로 검색..?
data1 = soup.find('a',{'class':'ofhd_float_back _BACK'})        # attr 생략 가능
data1 = soup.find('a', class_ = 'ofhd_float_back _BACK')        # 예약어 class_ 로도 가능

# print(data1)

data2 = soup.find('h2',attrs={'id':'title_area'})
data2 = soup.find('h2',{'id':'title_area'})
data2 = soup.find('h2',id ='title_area')
# print(data2)
# print(data2.get_text())

### find() - 1개만 검색, find_all() - 여러 개 검색(리스트로 출력)
data3 = soup.find('ul',{'class':'ranking_list'})
# li_data = data3.find('li',{'class':'rl_item _LAZY_LOADING_WRAP'})       # 맨 처음 것 한 개만
li_data = data3.find_all('li',{'class':'rl_item _LAZY_LOADING_WRAP'})   # 전부 출력
# print(data3)
print(len(li_data))
print(li_data)
print(li_data[1])

for li in li_data:
    li_title = li.find('p',{'class':'rl_txt'})
    print(li_title.get_text())