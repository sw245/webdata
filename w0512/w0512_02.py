
# import requests
from bs4 import BeautifulSoup   # parsing
import csv

# url = 'https://search.daum.net/search?w=tot&q=2024%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)

# res.raise_for_status()  # 에러 대비


with open('webdata/w0512/movies.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
    


# with open('webdata/w0512/movies.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# print(soup)

# print(soup.find('div',{'class':'pdt2'}))
# print(soup.find('div',{'id':'morColl'}))
# print(soup.find('c-list-doc'))


data = soup.find('c-list-doc')
# print(data)
# print(data.find_all('c-doc'))
doc = data.find_all('c-doc')
for d in doc:
    print(d.find('c-title'))
    print(d.find('c-contents-desc'))
    print(d.find('c-contents-desc-sub'))
























# # 파일 저장
# # ff = open('w0512/stock1.csv','w',encoding='utf-8-sig')



# title = []
# tdata = soup.find('thead')
# ths = tdata.find_all('th')
# for th in ths:
#     print(th.get_text().strip())
#     title.append(th.get_text().strip())




# ## 천 단위 표시 제거

# a = '123,456'
# b = a.replace(',','')
# print(b)
# sum = int(b) + 100
# print(sum)