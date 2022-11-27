import numpy as np
import time
from numpy.random import rand

N = 3

# numpy.dot 행렬곱
matA = np.array(rand(N, N))
matB = np.array(rand(N, N))
matC = np.dot(matA, matB)

# ndarray 1차원 백터, 2차원 행렬, 3차원 텐서
array1 = np.array([1,2,3,4,5])
array2 = np.array([[1,2,3,4], [5,6,7,8]])
array3 = np.array([[[1,2], [3,4], [5,6]]])

# 1차원 배열의 계산
storages = np.array([1,2,3,4])
storages += storages
storages ** 3 # 3승

# 인덱스 참조와 슬라이스
# 대입한 변수를 변경하면 참조하는 변수도 변경됨
# ndarray는 배열의 복사본이 아닌 view(원본)
# 파이썬의 list는 배열의 복사본
arr = np.arange(10)
arr[0:3] = 1
arr1 = np.array([1, 2, 3, 4])
arr2 = arr1
arr2[:] = 12
# 원본을 유지하기 위해 copy 메소드 사용
arr1 = np.array([1, 2, 3, 4])
arr2 = arr1.copy()
arr2[0] = 100

#Boolean 인덱스 참조
arr = np.array([2, 4, 6, 7])
arr[arr % 3 == 1]

#범용 함수
arr = np.array([1, 2, -3, 4, -5, 6])
#np.abs(arr) 절대값
#np.sqrt() 제곱근
#np.exp() 거듭제곱
#np.add()합
#np.substract() 요소 간의 차이
#np.maximum() 요소 간의 최댓값

# 집합 함수 - 1차원 배열만을 대상으로 한다.
arr1 = [1, 2, 3, 4, 2, 3]
arr2 = [4, 5, 2, 3]
#np.uniqued(x) x중복값 제거
#np.union1d(x, y) x와 y의 합집합
#np.intersect1d(x, y) x와 y의 교집합
#np.setdiff1d(x, y) x와 y의 차집합

# 난수
# 3 ~ 5 사이 2개 난수 생성
arr1 = np.random.randint(3, 5, 2)
# 0  ~ 1 미만의 난수
arr2 = np.random.rand()

# 2차원 배열
# 3개 배열 4개 요소
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# arr를 4행 3열로 반환
arr.reshape(4, 3)

# 인덱스 참조와 슬라이스
arr = np.array([[1, 2, 3], [4, 5, 6]])
# arr[1, 2] 1번 인덱스의 2번 원소
# arr[1, 1:] 1번 인덱스 1번부터 모두




