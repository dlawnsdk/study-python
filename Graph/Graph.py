import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import math
import time
from matplotlib import font_manager, rc
from mpl_toolkits.mplot3d import Axes3D
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
import datetime as dt
"""
시드 설정
"""
"""
X = np.random.rand(5)
Y = np.random.rand(5)
# 시드값을 고정하지 않으면 난수가 계속 바뀜
print("시드를 설정하지 않았을 때")


# 시드값 고정
np.random.seed(0)
X = np.random.randn(5)
np.random.seed(0)
Y = np.random.randn(5)
print("시드를 설정 했을 때")
print("X:", X)
print("Y:", Y)
"""

"""정규분포에 따른 난수 생성"""
"""
np.random.seed(0)
X = np.random.randn(10000)
# 데이터 시각화
plt.hist(X, bins='auto')
plt.show()
"""

"""이항분포에 따른 난수 생성"""
"""
np.random.seed(0)
# 0.5 확률로 100번 시도 했을 때 성공 횟수를 구하는 실험을 10000회 반복
nums = np.random.binomial(100, 0.5, size=10000)
print(nums.mean())
print(nums.mean()/100)
"""

"""리스트에서 무작위로 선택"""
"""
x = ["apple", "orange", "banana", "pineapple", "kiwifruit", "strawberry"]
np.random.seed(0)
y = np.random.choice(x, 5)
print(y)
"""

"""datetime형"""
"""
x = dt.datetime(1992, 10, 22)
print(x)
"""

"""timedelta형"""
# 기본 일, 초로 계산
# dt.timedelta(hours=1, minutes=30) 지정가능
"""
x = dt.timedelta(15, 360000)
print(x)
"""

"""datetime형과 timedelta형의 연산"""
"""
x = dt.datetime(1992, 10, 30)
y = x + dt.timedelta(5)
print(y)
"""

"""시각을 나타내는 문자열로 datetime 객체 만들기"""
"""
s = "1992-01-15"
x = dt.datetime.strptime(s, "%Y-%m-%d")
print(x)
"""

"""문자열을 숫자로 형 변환"""
"""
x = '64'
y = '16'
z = int(x) + int(y)
print(z)
"""

"""같은 간격의 수열 생성 - 1"""
"""
x = np.arange(0, 11, 2) #2개 간격으로 10까지 생성
print(x)
"""

"""같은 간격의 수열 생성하기 - 2"""
"""
x = np.linspace(0, 10, 3) # 3개 동일 간격으로 나눈다.
print(x)
"""

""""연습문제 - matplotlib"""
#np.random.seed(100)
# random_number_1 = np.random.rand(10000) # 균등 난수
# random_number_2 = np.random.randn(10000) # 정규분포
# random_number_3 = np.random.binomial(100, 0.8, size=(100000)) # 이항분포
#
# plt.figure(figsize=(10,10))
# plt.hist(random_number_1, bins=50)
# plt.title('uniform_distribution')
# plt.grid(True)
# #plt.show()
#
# plt.figure(figsize=(10,10))
# plt.hist(random_number_2, bins=50)
# plt.grid(True)
#plt.show()

# plt.figure(figsize=(10,10))
# plt.hist(random_number_3, bins=50)
# plt.grid(True)
# plt.show()

"""다양한 그래프 그리기"""
# days = np.arange(1, 11)
# weight = np.array([10, 14, 12, 18, 20, 16, 18, 17, 11, 21])
# plt.grid(True)
# plt.ylim([0, weight.max() + 1])
# plt.xlabel("days")
# plt.ylabel("weight")
#
# plt.plot(days, weight, marker="s", markerfacecolor="b")
# plt.show()

"""막대그래프"""
# x = [1, 2, 3, 4, 5, 6]
# y = [12, 23, 54, 44, 12, 98]
# 
# plt.bar(x, y)
# plt.show()

"""가로축에 라벨 설정"""
# x = [1, 2, 3, 4, 5, 6]
# y = [5, 2, 2, 1, 1, 1]
# labels = ["사원", "주임", "대리", "선임", "수석", "대표 이사"]
# plt.title("카이런소프트 임직원 현황")
# plt.bar(x, y, tick_label=labels, color="darkorange")
# plt.show()

"""누적 막대 그리기"""
# x = [1, 2, 3, 4, 5, 6]
# y1 = [12, 3, 54, 23, 81, 65]
# y2 = [32, 23, 54, 22, 12, 3]
# labels = ["orange", "apple", "kiwifruit", "banana", "pineapple", "strawberry"]
#
# plt.bar(x, y1, tick_label=labels)
# plt.bar(x, y2, bottom=y1)
#
# plt.legend(("y1", "y2"))
# plt.show()

"""히스토그램"""
# np.random.seed(0)
# data = np.random.randn(10000)
#
# plt.hist(data)
# plt.show()

"""구간수 설정하기"""
# np.random.seed(0)
# data = np.random.randn(10000)
# plt.hist(data, bins=100)
# plt.show()

"""정규화 하기"""
# np.random.seed(0)
# data = np.random.randn(10000)
# plt.hist(data, bins=100)
# plt.show()

"""누적 히스토그램 만들기"""
# np.random.seed(0)
# data = np.random.randn(10000)
# plt.hist(data, bins=100, cumulative=True)
# plt.show()

"""산포도"""
# np.random.seed(10)
# x = np.random.choice(np.arange(100), 100)
# y = np.random.choice(np.arange(100), 100)
# z = np.random.choice(np.arange(100), 100)

# z값을 기준으로 해당 데이터보다 값의 크기를 상대적으로 계산
# plt.scatter(x, y, marker="o", c=z, cmap="Greens")
# plt.colorbar()
# plt.show()

"""원그래프"""
# data = [60, 20, 10, 5, 3, 2]
# labels = ["Apple", "Orange", "Banana", "Pineapple", "Kiwifruit", "Strawberry"]
# explode = [0, .1, 0, 0, 0, 0]
# plt.pie(data, labels=labels, explode=explode)
# plt.axis("equal")
# plt.show()

"""3D 그래프"""
# t = np.linspace(-2*np.pi, 2*np.pi)
# X, Y = np.meshgrid(t, t)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# fig = plt.figure(figsize=(6, 6))
#
# ax = fig.add_subplot(1, 1, 1, projection="3d")
# ax.plot_surface(X, Y, Z)
# plt.show()

"""곡면 만들기"""
# x = y = np.linspace(-5, 5)
# X, Y = np.meshgrid(x, y)
# Z = np.exp(-(X**2 + Y**2)/2) / (2*np.pi)
# fig = plt.figure(figsize=(6, 6))
# ax = fig.add_subplot(1, 1, 1, projection="3d")
# ax.plot_surface(X, Y, Z)
# plt.show()

"""3D 히스토그램 만들기"""
# fig = plt.figure(figsize=(5, 5))
# ax = fig.add_subplot(111, projection="3d")
# 
# xpos = [i for i in range(10)]
# ypos = [i for i in range(10)]
# zpos = np.zeros(10)
# 
# dx = np.ones(10)
# dy = np.ones(10)
# dz = [i for i in range(10)]
# ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
# plt.show()

"""3D 산포도 만들기"""
# np.random.seed(0)
# X = np.random.randn(1000)
# Y = np.random.randn(1000)
# Z = np.random.randn(1000)
#
# fig = plt.figure(figsize=(6, 6))
# ax = fig.add_subplot(1, 1, 1, projection="3d")
#
# x = np.ravel(X)
# y = np.ravel(Y)
# z = np.ravel(Z)
# ax.scatter3D(X, Y, Z)
# plt.show()

"""3D 그래프에 컬러맵 적용하기"""
# t = np.linspace(-2*np.pi, 2*np.pi)
# X, Y = np.meshgrid(t, t)
#
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# fig = plt.figure(figsize=(6, 6))
# ax = fig.add_subplot(1, 1, 1, projection="3d")
# ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
# plt.show()

"""연습문제"""
# df_iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
# df_iris.columns = ["Sepal length", "sepal width", "petal length", "petal width", "class"]
# fig = plt.figure(figsize=(10,10))
#
# plt.scatter(df_iris.iloc[:50, 0], df_iris.iloc[:50, 1], label="setosa", color="k")
# plt.scatter(df_iris.iloc[50:100, 0], df_iris.iloc[50:100, 1], label="versicolor", color="b")
# plt.scatter(df_iris.iloc[100:150, 0], df_iris.iloc[100:150, 1], label="virginica", color="g")
# plt.xlabel("sepal length")
# plt.ylabel("sepal width")
# plt.legend(loc="best")
# plt.grid(True)
# plt.show()

"""종합문제"""
np.random.seed(100)
X = 0
N = 1000
circle_x = np.arange(0, 1, 0.001)
circle_y = np.sqrt(1 - circle_x * circle_x)

plt.figure(figsize=(5, 5))
plt.plot(circle_x, circle_y)
start_time = time.process_time()
for i in range(0, N):
    score_x = np.random.rand()
    score_y = np.random.rand()

    if score_x * score_x + score_y * score_y < 1:
        plt.scatter(score_x, score_y, marker='o', color="k")
        X = X + 1
    else:
        plt.scatter(score_x, score_y, marker='o', color="b")
pi = 4 * float(X)/float(N)

end_time = time.process_time()
time = end_time - start_time
print("원주율: %.6f" % pi)
print("실행시간: %f" % (time))

plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()