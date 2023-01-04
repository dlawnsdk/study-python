import pandas as pd

# ======================== Series ============================
#Series 데이터 예시(1)
fruits = {"Orange" : 1, "Banana" : 2}
series = pd.Series(fruits)
#print(series)

#Series 데이터 예시(2)
fruits = ["Orange", "Banana"]
count = [1,2]
# 인덱스 지정
series = pd.Series(fruits, index=count)
#print(series)

# 참조 예시
fruits = {"banana":3, "orange":4, "grape":1, "peach": 5}
series = pd.Series(fruits)
#print(series[0:2])
#print(series[["peach", "orange"]])

# 데이터와 인덱스 추출
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)
#print(series.values)
#print(series.index)

# 요소 추가
fruits = {"banana" : 3, "orange" : 5}
series = pd.Series(fruits)
grape = pd.Series([3], index={"grape"})
#series = series.append(grape) => 미래 버전에서 삭제될 예정
series = pd.concat([series, grape])
#print(series)

# 요소 삭제
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data = [10, 5, 3, 7, 2]
series = pd.Series(data, index=index)
series = series.drop("strawberry")
#print(series)

# 필터링(1)
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data = [10, 5, 2, 12, 3]
series = pd.Series(data, index=index)
condition = [True, True, False, False, True]
#print(series[condition])

# 필터링(2)
#print(series[series >= 5])
#print(series[series >= 5][series < 10])

# 정렬
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data = [10, 5, 2, 23, 3]
series = pd.Series(data, index=index)
#print(series.sort_index())
# ascending=False 내림차순
#print(series.sort_values(ascending=False))

# ======================== DataFrame ============================

# DataFrame 생성 예시
data = { "fruites" : ["apple", "orange", "banana", "strawberry", "kiwifruite"],
         "year": [2001,2002,2001,2008,2006],
         "time": [1,2,3,4,5] }
# 인덱스 지정, 지정하지 않으면 0부터 들어감
count = [1, 2, 3, 4, 5]
df = pd.DataFrame(data, index=count)
#print(df)

# Series를 이용하여 DataFormat 생성
index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
data1 = [10, 5,2, 12, 3]
data2 = [30, 23, 54, 12, 32]
series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)
# index 넣는 방법 1
count = [1, 2]
df = pd.DataFrame([series1, series2], index=count)
#print(df)

# index 넣는 방법 2
df = pd.DataFrame([series1, series2])
df.index = [3, 4]
#print(df)

# 행 추가
data = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
        "time": [1, 5, 6, 8, 9]}
df = pd.DataFrame(data)
series = pd.DataFrame({'fruits': ['orange'], 'time': ['20'], 'year': [2023]})
df = pd.concat([df, series], ignore_index=True)
#print(df)

# 열 추가
data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "year": [2001, 2002, 2008, 2006, 2002],
    "time": [1, 5, 2, 3, 8]
}
df = pd.DataFrame(data)
df["price"] = [150, 200, 130, 170, 220]
#print(df)

# 데이터 참조
data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "year": [2001, 2004, 2002, 2030, 2008],
    "time": [1, 6, 4, 2, 8]
}
df = pd.DataFrame(data)
df_loc = df.loc[[1, 2], ["time", "year"]] #이름으로 참조
df_iloc = df.iloc[[1, 2], [0, 2]] #번호로 참조

# 행 또는 열 삭제
data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "time": [1, 4, 5, 6, 3],
    "year": [2001, 2002, 2005, 2010, 2008]
}
df = pd.DataFrame(data)
df_1 = df.drop(range(0, 2)) # 0~1번 삭제
df_2 = df.drop("year", axis=1) # year 열 삭제

# 정렬
data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "time": [1, 1, 5, 2, 7],
    "year": [2005, 2002, 2008, 2005, 2006]
}
df = pd.DataFrame(data)

df = df.sort_values(by="year", ascending=True) # year 컬럼 기준 오름차순
df = df.sort_values(by=["time", "year"], ascending=True) # time으로 정렬 하는데 같은 경우 year로 정렬

# 필터링
data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "year": [2001, 2003, 2004, 2005, 2010],
    "time": [1, 4, 2, 6, 4]
}
df = pd.DataFrame(data)
#print(df.index % 2 == 0) # 인덱스가 짝수인 경우 True 홀수인 경우 False 출력
print(df[df.index % 2 == 0]) # 짝수 인덱스에 해당하는 데이터 출력


