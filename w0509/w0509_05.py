import requests
from bs4 import BeautifulSoup

# url = ''
# headers  = ''
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,'lxml')

# filehandle= open('w0509/a.html')
with open('w0509/a.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
    

# print(soup.title)
# print(soup.title.get_text())
# print(soup.h2)
# print(soup.find_all('h2'))
# print(soup.find('p',{'id':'p1'}).get_text())

# print(soup.find('ul'))
# print(soup.find('div',{'class':'c2'}).find('ul').find('li'))

# li_list = soup.find('ul').find_all('li')
# print(li_list[1].get_text())

# print(soup)
fruit_li = soup.find('div',{'class':'c2'}).find_all('li')
for l in fruit_li:
    print(l.get_text())
