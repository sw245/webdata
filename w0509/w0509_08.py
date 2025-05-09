
import requests
from bs4 import BeautifulSoup
import csv

## 웹이 아니니까 필요 없음?

# url = ''
# header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
# res = requests.get(url,header=header)


# html 태그 출력
# 태그 속성 출력 > find/find_all


with open('w0509/게시판3.html','r',encoding='utf8') as f:
    soup = BeautifulSoup(f,'lxml')


# 파일 저장
fileName = 'board.csv'
ff = open('w0509/'+fileName,'w',encoding='utf-8-sig',newline='')
writer = csv.writer(ff)


toptitle = []
# 제목부분 데이터

# ths = soup.thead.find_all('th')


# for i in range(len(ths)-1):
#     if i == 1 or i == 3:
#         print(ths[i].get_text(),end='\t\t')
#         toptitle.append(ths[i].get_text())
#     else:
#         print(ths[i].get_text(),end='\t')
#         toptitle.append(ths[i].get_text())
        

# writer.writerow(toptitle)       # 상단제목 > 파일에 저장  ## writer.writerow() 에는 리스트타입만 받음
# print()
# print('-'*60)


bodydata = []
# 게시글 부분 데이터
    
trs = soup.tbody.find_all('tr')

for tr in trs:
    tds = tr.find_all('td')
    # print(len(tds))
    if len(tds) > 1:
        for i in range(len(tds)-1):
            print(tds[i].get_text(),end='\t')
            bodydata.append(tds[i].get_text())
        print()
        
        ## 이런 식으로도 가능
        # for i,td in enumerate(tds):
        #     if i<5: print(td.get_text(),end='\t')
        # print()

        
# writer.writerow(bodydata)   # 파일에 게시글 저장
            
ff.close()
print("파일 저장완료")

