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
"""
인덱스나 컬럼이 일치하는DatFrame 2개 연결
axis=0: 세로
axis=1: 가로
"""
# columns = ["apple", "orange", "banana"]
# df_data1 = make_random_df(range(1, 5), columns, 0)
# df_data2 = make_random_df(range(1, 5), columns, 1)
# df1 = pd.concat([df_data1, df_data2], axis=0)
# df2 = pd.concat([df_data1, df_data2], axis=1)

"""
인덱스나 컬럼이 일치하지 않는 DataFrame간의 연결
"""
# columns1 = ["apple", "orange", "banana"]
# columns2 = ["orange", "kiwifruit", "banana"]
# 1, 2, 3, 4고 컬럼이 columns1인 DataFrame을 만든다.
#df_data3 = make_random_df(range(1, 5), columns1, 0)
# 인덱스가 1, 3, 5, 7이고, 컬럼이 columns2인 DataFrame을 만든다.(1부터7사이에 2개 간격으로 조회)
# df_data4 = make_random_df(np.arange(1, 8, 2), columns2, 1)
# df3 = pd.concat([df_data3, df_data4], axis=0)
# df4 = pd.concat([df_data3, df_data4], axis=1)

"""
연결 시 라벨 지정하기
"""
columns = ["apple", "orange", "banana"]
df_data5 = make_random_df(range(1, 5), columns, 0)
df_data6 = make_random_df(range(1, 5), columns, 1)

df = pd.concat([df_data5, df_data6], axis=1, keys=["df_data5", "df_data6"])
Y_banana = df["df_data6", "banana"]

print(df)
print()
print(Y_banana)





