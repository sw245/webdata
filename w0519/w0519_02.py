print(1+1)


# pandas의 1차원 데이터: Series
# - 1개 컬럼, 여러 개의 index


import pandas as pd

temp = pd.Series([-20,-10,0,10,20], index=['1월','2월','3월','4월','5월'])

# print(temp)
# print(temp['1월'])

# print(temp.sum())


# pandas의 2차원 데이터: DataFrame
# - 여러 개의 컬럼, 여러 개의 인덱스
# 구성 양식: 딕셔너리 안에 리스트 타입 ( 키: 컬럼, 밸류: 값 -리스트 형태 ) 

data = {
    '이름':['홍길동','유관순','이순신','강감찬','김구','김유신','홍길자','홍길순'],
    '학교':['가산고','가산고','가산고','가산고','가산고','디지털고','디지털고','디지털고'],
    '키':[197,184,168,187,188,202,188,190],
    '국어':[90,40,80,40,15,80,55,100],
    '영어':[85,35,75,60,20,100,65,85],
    '수학':[100,50,70,70,10,95,45,90],
    '과학':[95,55,80,75,35,85,40,95],
    '사회':[85,25,75,80,10,80,35,95],
    'SW특기':['Python','Java','Javascript','','','C','PYTHON','C#']
}

# print(data)

df = pd.DataFrame(data)

# print(df.describe())
# describe(): 데이터에서 숫자타입으로 구성된 컬럼의 기초적인 통계 제공

# print(df['키'].sum())
# print(df['키'].mean())

# print(df.values)        # 데이터를 리스트 타입으로
# print(df.index) 
# print(df.columns)


# print(df.info())
# info(): 데이터 유형 확인

# index 지정
df = pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
df.index.name = '지원번호'
print(df)

print(df.reset_index(drop=True,inplace=True))
print(df)



# DataFrame

# row > index
# column > column