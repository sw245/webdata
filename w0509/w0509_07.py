import requests
from bs4 import BeautifulSoup

with open('w0509/게시판3.html','r',encoding='utf8') as f:
    soup = BeautifulSoup(f,'lxml')
  
  
    
## find_previous_siblings()
## find_next_siblings()

data = soup.find('div',{'id':'input'})
data_div = soup.find('div',{'id':'input'}).find('div')
# data_s = data_div.find_next_sibling()       # 다음 형제 값 찾기
data_s = data_div.find_next_sibling().find_next_sibling()
# print(data.div.get_text())
# print(data_s)

# data2 = soup.find('thead').find('th').get_text()
# print(data2)

# th_list = soup.find('thead').find_all('th')
# for l in th_list:
#     print(l.get_text())
    
    
# html 태그 찾기
# print(soup.thead)     # 속성 지정 필요없을 경우
# print(soup.find('thead',{'class':''}))        # 속성 값도 지정해야 할 경우
# find_all()            # 결과 >> 리스트


# 자바스크립트를 읽지 못함.
data3 = soup.find('tbody',{'id':'tbody'})
trs = data3.find_all('tr')

# print(trs)

for tr in trs:
    tds = tr.find_all('td')
    if len(tds) >1:
        for td in tds:
            print(td.get_text())
# print(len(tds))
    
for tr in trs:
    tds = tr.find_all('td')
    if len(tds)>1:  # td가 1개면 출력하지 말 것
        for i in range(len(tds)-1): # 0,1,2,3,4
            print(tds[i].get_text(),end='\t')
        print()