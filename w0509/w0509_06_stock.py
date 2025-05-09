import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}

res = requests.get(url,headers=headers)     # requests로 url의 정보 가져오기
res.raise_for_status()                  # 에러 시 종료
soup = BeautifulSoup(res.text,'lxml')       # res.text 를 'lxml' 형식으로 변환

# print(soup.title)

# data1 = soup.find('div',{'class':'box_type_l'})
# trs = data1.tbody.find_all('tr')
# print(len(trs))
# print(trs[1])   # 삼성전자 tr

# print(trs)

# 6-10번 종목 출력
# for n in range(9,13+1):
#     print(trs[n])


### 종목 이름만 출력하기

print(soup)

