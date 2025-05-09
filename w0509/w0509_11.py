
from bs4 import BeautifulSoup
import csv

with open('w0509/join02_info_input.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
    
ff = open('w0509/items.csv','w',encoding='utf-8-sig',newline='')
writer = csv.writer(ff)
    
# print(soup.title)

dts = soup.find_all('dt')
# print(dts)

items = []

for dt in dts:
    if dt == dts[len(dts)-1]: continue
    print(dt.get_text())
    items.append(dt.get_text().strip())

# print(items)

writer.writerow(items)

# for la in labels_li:
#     print(la.get_text())


ff.close()