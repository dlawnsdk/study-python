import matplotlib.pyplot as plt
import numpy as np

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

"""그래프에 데이터 표시학"""

# x = np.linspace(0, 2*np.pi)
#
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()

"""그래프의 표시 범위 설정하기"""

# x = np.linspace(0, 2*np.pi)
# y = np.sin(x)
#
# plt.ylim([-1, 1]) # y축 범위 설정
# plt.plot(x, y)
# plt.show()


"""그래프 요소에 이름 설정하기"""

# x = np.linspace(0, 2 * np.pi)
# y = np.sin(x)
#
# plt.title("맷플롯립")
# plt.xlabel("기간")
# plt.ylabel("이름")
#
# plt.grid(True) # 그래프에 그리드 추가
#
# plt.plot(x, y)
# plt.show()


"""그래프 축에 눈금 설정하기"""

# x = np.linspace(0, 2 * np.pi)
# y = np.sin(x)
#
# plt.title("y=sin(x)")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
#
# plt.grid(True)
#
# positions = [0, np.pi/2, np.pi, np.pi*3/2, np.pi*2] # 눈금을 삽입할 위치
# labels = ["0º", "90º", "180º", "270º", "360º"] # 삽입할 눈금
#
# plt.xticks(positions, labels)
# plt.plot(x, y)
# plt.show()


"""여러 데이터 시각화하기(1)"""

# x = np.linspace(0, 2 * np.pi)
# y1 = np.sin(x)
# y2 = np.cos(x)
# labels = ["90º", "180º", "270º", "360º"]
# positions = [np.pi/2, np.pi, np.pi*3/2, np.pi*2]
#
# plt.title("Graphs of Trigonometric Funtions")
#
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
#
# plt.grid(True)
# plt.xticks(positions, labels)
#
# plt.plot(x, y1, color="b")
# plt.plot(x, y2, color="g")
# plt.show()


"""여러 데이터 시각화하기(2)"""

# x = np.linspace(0, 2 * np.pi)
# y = np.sin(x)
#
# plt.figure(figsize=(4, 4)) # 그림의 크기
# plt.plot(x, y)
# plt.show()


"""서브플롯 만들기"""
# x = np.linspace(0, 2 * np.pi)
# y = np.sin(x)
#
# fig = plt.figure(figsize=(9, 6))
#
# ax = fig.add_subplot(2, 3, 5)
#
# ax.plot(x, y)
#
# axi = []
# for i in range(6):
#     if i == 4:
#         continue
#     fig.add_subplot(2, 3, i + 1)
# plt.show()

"""서브플롯 주변의 여백 조정하기"""
x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

labels = ["90º", "180º", "270º", "360º"]
positions = [np.pi/2, np.pi, np.pi*3/2, np.pi*2]

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(2, 3, 6)
plt.subplots_adjust(wspace=1, hspace=1)

ax.plot(x, y)

axi = []
for i in range(6):
    if i == 5:
        continue
    fig.add_subplot(2, 3, i+1)
plt.show()
