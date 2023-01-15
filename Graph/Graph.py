import numpy as np
import matplotlib.pyplot as plt

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
np.random.seed(0)
# 0.5 확률로 100번 시도 했을 때 성공 횟수를 구하는 실험을 10000회 반복
nums = np.random.binomial(100, 0.5, size=10000)
print(nums.mean())
print(nums.mean()/100)