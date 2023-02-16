import pandas as pd
import numpy as np
from numpy import nan as NA
from pandas import Series, DataFrame
import csv

# df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
# df.columns=["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/0D315 of diluted wines", "Proline"]
# print(df)

# df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
# df.columns=["sepal length", "sepal width", "petal length", "petal width", "class"]
# print(df)

"""CSV 라이브러리로 csv 파일 만들기"""
# with open("csv0.csv", "w") as csvfile:
#     writer = csv.writer(csvfile, lineterminator="\n")
#
#     writer.writerow(["city", "year", "season"])
#     writer.writerow(["Nagano", 1998, "winter"])
#     writer.writerow(["Sydney", 2000, "Summer"])

"""Pandas로 csv 파일 만들기"""
# data = {
#     "city": ["Nagano", "Sydney", "Salt Lake City", "Athens", "Torino", "Beijing", "Vancouver", "London", "Sochi", "Rio de Janerio"],
#     "year": [1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016],
#     "session": ["Windter", "Summer", "Winter", "Summer", "Winter", "Summer", "Winter", "Summer", "Winter", "Summer"]
# }
# df = pd.DataFrame(data)
# df.to_csv("csv1.csv")

"""DataFrame 연습"""
# attri_data1 = {
#     "ID": ["100", "101", "102", "103", "104", "106", "108", "110", "111", "113"],
#     "city": ["서울", "부산", "대전", "광주", "서울", "서울", "부산", "대전", "광주", "서울"],
#     "birth_year": [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
#     "name": ["영이", "순돌", "짱구", "태양", "션", "유리", "현아", "태식", "민수", "호식"]
# }
# attri_data2 = {
#     "ID": ["107", "109"],
#     "city": ["봉화", "전주"],
#     "birth_year": [1994, 1988]
# }
#
# attri_data_fram1 = DataFrame(attri_data1)
# attri_data_fram2 = DataFrame(attri_data2)
# attri_data_fram3 = pd.concat([attri_data_fram1, attri_data_fram2]).sort_values(by="ID", ascending=True).reset_index(drop=True)
# print(attri_data_fram3)

"""결측치? 누락된 값(NULL)"""
# sample_data_frame = pd.DataFrame(np.random.rand(10, 4))
# sample_data_frame.iloc[1, 0] = NA
# sample_data_frame.iloc[8, 2] = NA
# list_wise_deletion = sample_data_frame.dropna() # 리스트와이즈 삭제: 모든 변수가 정확한 값으로 채워져 있는 관측치만을 대상으로 분석하는 방법
# pairwise_deletion = sample_data_frame[[0, 1, 2]].dropna() # 페어와이즈 삭제: 분석에서 사용되는 변수에 결측치가 있을 때 CASE를 지우고 분석하는 방법
# print(pairwise_deletion)

"""결측치 보완"""
# sample_data_frame = pd.DataFrame(np.random.rand(10, 4))
# sample_data_frame.iloc[1, 0] =NA
# sample_data_frame.iloc[2, 2] =NA
# sample_data_frame.iloc[5:, 3] =NA
# print(sample_data_frame.fillna(0)) # NaN을 0으로 치환
# print(sample_data_frame.fillna(method="ffill")) # Nan인 경우 이전 데이터 주입

"""결측치 보완(평균값 대입법)"""
# sample_data_frame = pd.DataFrame(np.random.rand(10, 4))
# sample_data_frame.iloc[1, 0] = NA
# sample_data_frame.iloc[2, 2] = NA
# sample_data_frame.iloc[5:, 3] = NA
# 
# sample_data_frame_mean = sample_data_frame.fillna(sample_data_frame.mean())
# print(sample_data_frame_mean)

"""키별 통계량 산출"""
# df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
# df.columns=["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/0D315 of diluted wines", "Proline"]
#
# print(df["Magnesium"].mean())

"""중복 데이터"""
# dupli_data = DataFrame({
#     "col1": [1, 1, 2, 3, 4, 4, 6, 6],
#     "col2": ["a", "a", "b", "b", "b", "c", "b", "b"]
# })
# print(dupli_data.duplicated())
#
# drop_duplicate = dupli_data.drop_duplicates() # 중복 행 제거
# print(drop_duplicate)

# dupli_data = DataFrame(
#     {
#         "col1": [1, 1, 2, 3, 4, 4, 6, 6, 7, 7, 7, 8, 9, 9],
#         "col2": ["a", "b", "b", "b", "c", "c", "b", "b", "d", "d", "c", "b", "c", "c"]
#      }
# )
# print(dupli_data.drop_duplicates())

"""매핑"""

#
# attri_data_frame1 = DataFrame(attri_data1)
# city_map = {
#     "서울":"서울",
#     "광주": "전라도",
#     "부산": "경상도",
#     "대전": "충청도"
# }
# attri_data_frame1["region"] = attri_data_frame1["city"].map(city_map)
# MS_map = {
#     "서울": "중부",
#     "대전": "중부",
#     "광주": "남부",
#     "부산": "남부"
# }
# attri_data_frame1["MS"] = attri_data_frame1["city"].map(MS_map)
# print(attri_data_frame1.to_html('chiron.html'))

# attri_data1 = {
#     "ID": ["100", "101", "102", "103", "104", "106", "108", "110", "111", "113"],
#     "city": ["서울", "부산", "대전", "광주", "서울", "서울", "부산", "대전", "광주", "서울"],
#     "birth_year": [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
#     "name": ["영이", "순돌", "짱구", "태양", "션", "유리", "현아", "태식", "민수", "호식"]
# }
# 
# attri_data_frame1 = DataFrame(attri_data1)
# birth_year_bins = [1980, 1985, 1990, 1995, 2000]
# label = ["1번", "2번"]
# birth_year_cut_data = pd.cut(attri_data_frame1.birth_year, 2, labels=label)
# print(birth_year_cut_data)

"""연습문제"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df.colums = [
    "", "Alcohol", "Mail acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "NonFlavanoid phenols", "Proanthocyanins",
    "Color intensity", "Hue", "OD280/0D315 of diluted wines", "Proline"
         ]
df_ten = df.head(10)
df_ten.iloc[1, 0] = NA
df_ten.iloc[2, 3] = NA
df_ten.iloc[4, 8] = NA
df_ten.iloc[7, 3] = NA
print(df_ten)