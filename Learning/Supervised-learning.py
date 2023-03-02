import matplotlib.cm
import numpy as np
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# X, y = make_classification(n_samples=50, n_features=2, n_redundant=0, random_state=0)
# plt.scatter(X[:, 0], X[:, 1], c=y, marker=".", cmap=matplotlib.colormaps.get_cmap("bwr"), alpha=0.7)
# plt.grid(True)
# plt.show()

"""학습과 예측"""
# 데이터 생성
# X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)
# # 데이터를 학습용과 평가용으로 구분
# train_X, test_X, train_Y, test_y = train_test_split(X, y, random_state=42)
# # 모델 구축
# model = LogisticRegression(random_state=42)
# # 모델 학습
# model.fit(train_X, train_Y)
# pred_x = model.predict(test_X)
# print(pred_x)

"""로지스틱 회귀"""
# 데이터 생성
x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)
train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=42)
# 모델 구축
model = LogisticRegression()
# 모델 학습
model.fit(train_x, train_y)
# 예측 결과 도출
pred_x = model.predict(test_x)
# 데이터를 플롯
plt.scatter(x[:, 0], x[:, 1], c=y, marker=".", cmap=matplotlib.colormaps.get_cmap("bwr"), alpha=0.7)
# 식별 경계선 플롯
xi = np.linspace(-10, 10)
Y = -model.coef_[0][0] / model.coef_[0][1] * xi - model.intercept_ / model.coef_[0][1]
plt.plot(xi, Y)
# 그래프 스케일 조정
plt.xlim(min(x[:, 0]) - 0.5, max(x[:, 0]) + 0.5)
plt.ylim(min(x[:, 1]) - 0.5, max(x[:, 1]) + 0.5)
# 제목
plt.title("Classfication data using LogisticRegression")
# x축 y축 이름 설정
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()