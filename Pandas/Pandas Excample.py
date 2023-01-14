import random

import numpy as np
import pandas as pd

# DataFrame 연결 - 1

# 지정한 인덱스와 컬럼을 가진 DataFrame을 난수로 생성하는 함수
def make_random_df(index, columns, seed):
    # np.random.seed: 같은 값의 파라미터가 들어오면 같은 난수 생성
    np.random.seed(seed)
    df = pd.DataFrame()
    for column in columns:
        # random.choice: 한개 원소를 뽑는다.
        df[column] = np.random.choice(range(1, 101), len(index))
    df.index = index
    return df

"""인덱스나 컬럼이 일치하는DatFrame 2개 연결
axis=0: 열
axis=1: 행
"""
# columns = ["apple", "orange", "banana"]
# df_data1 = make_random_df(range(1, 5), columns, 0)
# df_data2 = make_random_df(range(1, 5), columns, 1)
# df1 = pd.concat([df_data1, df_data2], axis=0)
# df2 = pd.concat([df_data1, df_data2], axis=1)

"""인덱스나 컬럼이 일치하지 않는 DataFrame간의 연결"""
# columns1 = ["apple", "orange", "banana"]
# columns2 = ["orange", "kiwifruit", "banana"]
# 1, 2, 3, 4고 컬럼이 columns1인 DataFrame을 만든다.
#df_data3 = make_random_df(range(1, 5), columns1, 0)
# 인덱스가 1, 3, 5, 7이고, 컬럼이 columns2인 DataFrame을 만든다.(1부터7사이에 2개 간격으로 조회)
# df_data4 = make_random_df(np.arange(1, 8, 2), columns2, 1)
# df3 = pd.concat([df_data3, df_data4], axis=0)
# df4 = pd.concat([df_data3, df_data4], axis=1)

"""연결 시 라벨 지정하기"""
# columns = ["apple", "orange", "banana"]
# df_data5 = make_random_df(range(1, 5), columns, 0)
# df_data6 = make_random_df(range(1, 5), columns, 1)

# df = pd.concat([df_data5, df_data6], axis=1, keys=["df_data5", "df_data6"])
# Y_banana = df["df_data6", "banana"]
# print(df)
# print()
# print(Y_banana)

"""
내부 결합 - 일치하지 않는 행은 삭제
"""
"""
#data1 = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "year": [2001, 2002, 2003, 2008, 2006],
    "amount": [1, 4, 5, 6, 3]
#}
#df1 = pd.DataFrame(data1)

data2 = {
    "fruits": ["apple", "orange", "banana", "strawberry", "mango"],
    "year": [2001, 2002, 2001, 2008, 2009],
    "price": [150, 120, 170, 200, 150]
}
df2 = pd.DataFrame(data2)

df3 = pd.merge(df1, df2, on="fruits", how="inner")
print(df3)
"""

"""외부 결합 - 일치하는 행이 아니라도 삭제되지 않고 NaN으로 표기"""
"""
data1 = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "year": [2001, 2002, 2008, 2006, 2010],
    "amount": [1, 5, 2, 8, 9]
}
df1 = pd.DataFrame(data1)
data2 = {
    "fruits": ["apple", "banana", "strawberry", "kiwifruit", "mango"],
    "year": [2001, 2002, 2003, 2009, 2010],
    "price": [150, 120, 100, 250, 3000]
}
df2 = pd.DataFrame(data2)
df3 = pd.merge(df1, df2, on="fruits", how="outer")
print(df3)
"""

"""이름이 다른 열을 KEY로 결합하기"""
"""
order_df = pd.DataFrame([
    [1000, 2549, 103],
    [1001, 2938, 101],
    [1002, 2777, 101]],
    columns=["id", "item_id", "customer_id"]
)
custer_df = pd.DataFrame([
    [101, "준아"],
    [102, "민호"],
    [103, "지희"]],
    columns=["id", "name"]
)
# 왼쪽 DF에서 사용할 id와 오른쪽 DF에서 사용할 id 설정
order_df = pd.merge(order_df, custer_df, left_on="customer_id", right_on="id", how="inner")
print(order_df)
"""

"""인덱스를 KEY로 결합하기"""
"""
order_df = pd.DataFrame(
    [[101, 2546, 103],
    [1001, 342, 101],
    [1002, 342, 101]],
    columns=["id", "item_id", "customer_id"]
)
customer_df = pd.DataFrame(
    [["광수"],
     ["민호"],
     ["소희"]],
    columns=["name"]
)
customer_df.index = [101, 102, 103]
# 왼쪽 DF customer_id와 오른쪽 DF의 index가 같은 데이터 추출
order_df = pd.merge(order_df, customer_df, left_on="customer_id", right_index=True, how="inner")
print(order_df)
"""

"""특정 행 얻기"""
"""
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
df.index = range(1, 11)
# 위에서 3개 행
df_head = df.head(3)
# 아래서 3개 행
df_tail = df.tail(3)
print(df_tail)
"""

"""계산 처리하기"""
"""
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
df.index = range(1, 11)
# x2
double_df = df * 2
# 제곱
square_df = df ** 2
# 제곱근
sqrt_df = np.sqrt(df) 
"""

"""통계 정보 얻기"""
"""
np.random.seed(0)
columns = ["apple", "orange", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
df.index = range(1, 11)
# describe(): 컬럼당 데이터 수, 평균값, 표준편차, 최솟값, 최댓값, 사분위수를 인덱스로 계산
df_des = df.describe().loc[["mean", "max", "min"]]
print(df_des)
"""

"""DataFrame의 행간 차이와 열간 차이 구하기"""
"""
np.random.seed(0)
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
df = pd.DataFrame()
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
df.index = range(1, 11)
# diff: 행간 차이를 구한다. -2한 행과의 차이를 구한다.
df_diff = df.diff(-2, axis=0)
print(df_diff)
"""

"""그룹화"""
"""
prefecture_df = pd.DataFrame(
    [
        ["강릉", 1040, 213527, "강원도"],
        ["광주", 430, 1458915, "전라도"],
        ["평창", 1463, 42218, "강원도"],
        ["대전", 539, 1476955, "충청도"],
        ["단양", 780, 29816, "충청도"]
    ],
    columns=["Prefecture", "Area", "Population", "Region"]
)
# 그룹화
groupby_region = prefecture_df.groupby("Region")
# 그룹화한 데이터의 평균
mean_df = groupby_region.mean()
print(mean_df)
"""

"""최종 연습문제"""
"""
df1 = pd.DataFrame(
    [
        ["apple", "Fruit", 120],
        ["orange", "Fruit", 60],
        ["banana", "Fruit", 100],
        ["pumpkin", "Vegetable", 150],
        ["potato", "Vegetable", 80]
    ],
    columns=["Name", "Type", "Price"]
)
df2 = pd.DataFrame(
    [
        ["onion", "Vegetable", 60],
        ["carrot", "Vegetable", 50],
        ["beans", "Vegetable", 100],
        ["grape", "Vegetable", 80]
    ],
    columns=["Name", "Type", "Price"]
)

# df1 + df2 컬럼 연결
df3 = pd.concat([df1, df2], axis=0)
# 컬럼 Type의 값이 Fruit인 행 조회
df_fruit =df3.loc[df3["Type"] == "Fruit"]
# Price를 기준으로 정렬
df_fruit = df_fruit.sort_values(by="Price", ascending=True)
# 컬럼 Type의 값이 Vegetable인 행 조회
df_veg = df3.loc[df3["Type"] == "Vegetable"]
# Price를 기준으로 정렬
df_veg = df_veg.sort_values(by="Price", ascending=True)
# Price의 값이 작은 3개의 과일과 야채의 합
result = sum(df_fruit[:3]["Price"]) + sum(df_veg[:3]["Price"])
print(result)
"""

"""최종 종합문제"""
index = ["광수", "민호", "소회", "태양", "영희"]
columns = ["국어", "수학", "사회", "과학", "영어"]
data = [
    [30, 24, 90, 65, 58],
    [68, 30, 67, 66, 45],
    [67, 88, 35, 98, 22],
    [55, 66, 65, 89, 47],
    [76, 56, 89, 23, 44]
]
df = pd. DataFrame(data, index=index, columns=columns)
# "체육" 컬럼 및 데이터 추가
pe_column = pd.Series(
    [55, 66, 65, 89, 47],
    index=["광수", "민호", "소희", "태양", "영희"]
)
df["체육"] = pe_column
# INDEX 수학으로 정렬
df1 = df.sort_values(by="수학", ascending=True)
# +5
df2 = df1 + 5
# 평균, 최대, 최소 값조회
df3 = df2.describe().loc[["mean", "max", "min"]]
print(df3)
