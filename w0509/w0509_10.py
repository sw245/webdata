
from bs4 import BeautifulSoup

import csv

with open('w0509/notice_list.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
    
# 파일 저장
fileName = 'notice_list.csv'
ff = open('w0509/'+fileName,'a',encoding='utf-8-sig',newline='')        # sig 처리를 하지 않으면 엑셀파일에서 열 때 파일이 깨짐..
writer = csv.writer(ff)     # csv파일 저장

titlecsv = []

# 타이틀
ths = soup.table.find_all('th')
for th in ths:
    print(th.get_text(),end='\t')
    titlecsv.append(th.get_text())
print()
    
writer.writerow(titlecsv)
    

contentcsv = []
    
# 내용
trs = soup.table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        print(td.get_text(),end='\t')
        contentcsv.append(td.get_text())
    print()

writer.writerow(contentcsv)

## 홀수 번째 게시글만
# print(len(trs)) == 11

# for i in range(len(trs)):
#     if i % 2 == 1:
#         tds = trs[i].find_all('td')
#         for td in tds:
#             print(td.get_text(),end='\t')
#     print()
    
    
    