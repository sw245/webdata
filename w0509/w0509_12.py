import requests
from bs4 import BeautifulSoup
import csv

url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page=1'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)


res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

ff = open('w0509/stock.csv','w',encoding='utf-8-sig',newline='')
writer = csv.writer(ff)

# stock_title = []

# ths = soup.thead.find_all('th')
# for th in ths:
#     print(th.get_text(),end='\t')
#     stock_title.append(th.get_text())
    
# writer.writerow(stock_title)

# print(soup.thead.get_text())


# print(len(soup.tbody.find_all('tr')))

stock = []

trs = soup.tbody.find_all('tr')
n = 0
for tr in trs:
    if n == 5: break
    tds = tr.find_all('td')
    # print(len(tr.find_all('td')))
    
    if len(tds) < 2: continue
    
    for td in tds:
        print(td.get_text().strip(),end='\t')
        stock.append(td.get_text().strip())
    print()
    n += 1

writer.writerow(stock)


ff.close()


