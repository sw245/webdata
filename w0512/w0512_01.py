import requests
from bs4 import BeautifulSoup   # parsing
import csv


ff = open('webdata/w0512/stock1.csv','a',encoding='utf-8-sig',newline='')
writer = csv.writer(ff)

for j in range(1,6):
    url = f'https://finance.naver.com/sise/sise_market_sum.naver?&page={j}'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
    res = requests.get(url,headers=headers)

    res.raise_for_status()  # 에러 대비

    soup = BeautifulSoup(res.text,'lxml')


    # 파일 저장
    if j == 1:
        title = []

        tdata = soup.find('thead')
        ths = tdata.find_all('th')
        for th in ths:
            title.append(th.get_text().strip())
            

        writer.writerow(title)


# print(soup)
# print(soup.find('thead'))
# print(soup.thead.find_all('th'))
# print(soup.thead.find('th',{'class':'tr'}))
# print(soup.thead.find('th',{'class':'tr'}).get_text())

    trs = soup.tbody.find_all('tr')
# print(trs[1])
# print(soup.tbody.tr.find_next_sibling())

# tds_samsung = trs[1].find_all('td')
# print(trs[1].find_all('td'))
# for td in tds_samsung:
#     print(td.get_text().strip())
# tds_hynix = trs[2].find_all('td')
# for td in tds_hynix:
#     print(td.get_text().strip())
    
    for tr in trs:
        tds = tr.find_all('td')
        if len(tds) < 2: continue
        contents = []
        for i,td in enumerate(tds):
            if i == 3:
                # print(td.em.span.get_text())
                # print(td.em.find_next_sibling().get_text().strip())
                contents.append(td.em.span.get_text())
                contents.append(td.em.find_next_sibling().get_text().strip())
            elif i == 12:
                continue
            else:
                # print(td.get_text().strip())
                contents.append(td.get_text().strip())
        writer.writerow(contents)
        print('-'*30)
    

    
# sum = 0

# for tr in trs:
#     td_price = tr.find('td',{'class':'number'})
#     if td_price == None: continue
#     price = int(td_price.get_text().replace(',',''))
#     print(price)
#     sum += price
# print("-"*20)
# print(f'{sum:,d}')


ff.close()