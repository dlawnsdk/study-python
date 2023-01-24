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
# x = np.linspace(0, 2 * np.pi)
# y = np.sin(x)
# 
# labels = ["90º", "180º", "270º", "360º"]
# positions = [np.pi/2, np.pi, np.pi*3/2, np.pi*2]
# 
# fig = plt.figure(figsize=(9, 6))
# ax = fig.add_subplot(2, 3, 6)
# plt.subplots_adjust(wspace=1, hspace=1)
# 
# ax.plot(x, y)
# 
# axi = []
# for i in range(6):
#     if i == 5:
#         continue
#     fig.add_subplot(2, 3, i+1)
# plt.show()

"""서브플롯의 그래프 표시 범위 설정하기"""
# x = np.linspace(0, 2*np.pi)
# y = np.sin(x)
# labels = ["90º", "180º", "270º", "360º"]
# positions = [np.pi/2, np.pi, np.pi*3/2, np.pi*2]
#
# fig = plt.figure(figsize=(9, 6))
# ax = fig.add_subplot(2, 3, 5)
#
# plt.subplots_adjust(wspace=1, hspace=1)
#
# ax.plot(x, y)
# ax.set_ylim(0, 1) # y축을 0~1로 설정
# axi = []
# for i in range(6):
#     if i == 4:
#         continue
#     fig.add_subplot(2, 3, i+1)
# plt.show()

"""서브플롯의 그래프 요소에 이름 설정하기"""
# x = np.linspace(0, 2 * np.pi)
# y = np.sin(x)
# labels = ["90º", "180º", "270º", "360º"]
# positions = [np.pi/2, np.pi, np.pi * 3/2, np.pi * 2]
#
# fig = plt.figure(figsize=(9, 6))
# ax = fig.add_subplot(2, 3, 5)
# plt.subplots_adjust(wspace=1.0, hspace=1.0)
# ax.plot(x, y)
# ax.set_title("Study AI for Jun")
# ax.set_xlabel("x축")
# ax.set_ylabel("y축")
# axi = []
# for i in range(6):
#     if i == 4:
#         continue
#     fig.add_subplot(2, 3, i+1)
# plt.show()

"""서브플롯 그래프에 그리드 표시하기"""
# x = np.linspace(0, 2 * np.pi)
# y = np.sin(x)
#
# fig = plt.figure(figsize=(9, 6))
# ax = fig.add_subplot(2, 3, 5)
#
# plt.subplots_adjust(wspace=1.0, hspace=1)
# ax.grid(True)
# ax.set_title("Show Grid")
# ax.set_xlabel("x축")
# ax.set_ylabel("y축")
# ax.plot(x, y)
# axi = []
# for i in range(6):
#     if i == 4:
#         continue
#     fig.add_subplot(2, 3, i + 1)
# plt.show()

"""서브플롯 그래프 축에 눈금 설정하기"""
# x = np.linspace(0, 2 * np.pi)
# y = np.sin(x)
# positions = [0, np.pi/2, np.pi, np.pi*3/2, np.pi*2]
# labels = ["0º", "90º", "180º", "270º", "360º"]
#
# fig = plt.figure(figsize=(9, 6))
# ax = fig.add_subplot(2, 3, 5)
#
# plt.subplots_adjust(wspace=1, hspace=1)
# ax.grid(True)
# ax.set_title("Grid Setting")
# ax.set_xlabel("x axis")
# ax.set_ylabel("y axis")
#
# # 서브플롯 그래프에 눈금 설정
# ax.set_xticks(positions)
# ax.set_xticklabels(labels)
#
# ax.plot(x, y)
#
# axi = []
# for i in range(6):
#     if i == 4:
#         continue
#     fig.add_subplot(2, 3, i + 1)
# plt.show()

"""연습문제"""
x_upper = np.linspace(0, 5)
x_lower = np.linspace(0, np.pi * 2)
x_tan = np.linspace(-np.pi/2, np.pi/2)
positions_upper = [i for i in range(5)]
positions_lower = [0, np.pi/2, np.pi, np.pi*3, np.pi*2]
positions_tan = [-np.pi/2, 0, np.pi/2]
labels_upper = [i for i in range(5)]
labels_lower = ["0º", "90º", "180º", "270º", "360º"]
labels_tan = ["-90º", "0º", "90º"]

fig = plt.figure(figsize=(9, 6))
plt.subplots_adjust(wspace=0.4, hspace=0.4)
for i in range(3):
    y_upper = x_upper ** (i + 1)
    ax = fig.add_subplot(2, 3, i + 1)
    ax.grid(True)
    ax.set_title("$y=x^%i$" % (i + 1))
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_xticks(positions_upper)
    ax.set_xticklabels(labels_upper)
    ax.plot(x_upper, y_upper)

y_lower_list = [np.sin(x_lower), np.cos(x_lower)]
title_list = ["$y=sin(x)$", "$y=cos(x)$"]
for i in range(2):
    y_lower = y_lower_list[i]
    ax = fig.add_subplot(2, 3, i + 4)
    ax.grid(True)
    ax.set_title(title_list[i])

    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")

    ax.set_xticks(positions_lower)
    ax.set_xticklabels(labels_lower)

    ax.plot(x_lower, y_lower)

ax = fig.add_subplot(2, 3, 6)

ax.grid(True)

ax.set_title("$y=tan(x)$")

ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")

ax.set_xticks(positions_tan)
ax.set_xticklabels(labels_tan)

ax.set_ylim(-1, 1)

ax.plot(x_tan, np.tan(x_tan))

plt.show()



