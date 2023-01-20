import numpy as np
import matplotlib.pyplot as plt
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
random_number_1 = np.random.rand(10000) # 균등 난수
random_number_2 = np.random.randn(10000) # 정규분포
random_number_3 = np.random.binomial(100, 0.8, size=(100000)) # 이항분포

plt.figure(figsize=(10,10))
plt.hist(random_number_1, bins=50)
plt.title('uniform_distribution')
plt.grid(True)
#plt.show()

plt.figure(figsize=(10,10))
plt.hist(random_number_2, bins=50)
plt.grid(True)
#plt.show()

plt.figure(figsize=(10,10))
plt.hist(random_number_3, bins=50)
plt.grid(True)
plt.show()







