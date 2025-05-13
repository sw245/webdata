import requests
from bs4 import BeautifulSoup

for i in range(1,6):
    url = f'https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2025-05-16&checkOut=2025-05-17&personal=2&freeForm=false&page={i}'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
    res = requests.get(url,headers=headers)

    res.raise_for_status()

    soup = BeautifulSoup(res.text,'lxml')


    # 제목, 평점, 평가 인원 수, 가격, 이미지 url

    alis = soup.find('div',{'class':'css-1qumol3'}).find_all('a',{'class':'gc-thumbnail-type-seller-card css-wels0m'})
    # n = 0

    for a in alis:
        
        title = a.find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1gxx2ac'}).get_text()
        rate = a.find('span',{'class':'css-9ml4lz'}).get_text()
        # if float(rate) >= 9.1:
        #     print(rate)
        reviews = a.find('span',{'class':'css-oj6onp'}).get_text()[:-4]
        # if int(reviews.replace(',','')) >= 1000:
        #     print(reviews)
        try: price = a.find('span',{'class','css-5r5920'}).get_text()
        except: pass

        print(f'{title}\t{rate}\t{reviews}\t{price}')
        # if price != None:         # None일 때 get_text()가 에러 남
        #     print(price.get_text())
        
        # print(a.find('div',{'class':'css-nl3cnv'}))
        
