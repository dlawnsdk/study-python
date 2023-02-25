import matplotlib.pyplot as plt
import cv2
import numpy as np
import time
import os

img = cv2.imread("D:/python/python-study/img/pythonImage.png", cv2.IMREAD_COLOR)

"""이미지 읽기"""
# cv2.imshow("sample", img)
# cv2.waitKey(0) # 이미지가 보여지는 시간을 인수로 넣는다.(0을 넣으면 무한)
# cv2.destroyAllWindows() # 창 종료

"""이미지 쓰기"""
# img_size = (512, 512)
# my_img = np.array([[[255, 255, 255] for _ in range(img_size[1])] for _ in range(img_size[0])], dtype="uint8")
# cv2.imshow("sample", my_img)
# cv2.imwrite("my_red_img.jpg", my_img)

"""트리밍, 리사이즈"""
# size = img.shape
# my_img = img[: size[0] // 2, : size[1] // 3] # 가로 세로 크기를 나눈다.(이미지의 일부분 == 트리밍)
# my_img = cv2.resize(my_img, (my_img.shape[1] * 2, my_img.shape[0] * 2)) # 폭, 높이 크기를 *2
# cv2.imshow("sample", my_img)
# cv2.waitKey(0)

"""회전 및 반전"""
# mat = cv2.getRotationMatrix2D(tuple(np.array(img.shape[:2]) / 2), 180, 1) # 행렬 생성 -> 회전 중심, 회전 각도, 비율
# # my_img = cv2.warpAffine(img, mat, img.shape[:2])
# my_img = cv2.flip(img, 1) # 0: x축 양수: y축 음수: 두 축을 기준으로 반전
# cv2.imshow("sample", my_img)
# cv2.waitKey(0)

"""색조 변환 및 색상 반전"""
# my_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # RGB2LAB, RGB2GRAY
# my_img = cv2.bitwise_not(img) # 네거티브 반전
# cv2.imshow("sample", my_img)
# cv2.waitKey(0)

"""임계값 처리"""
# retaval, my_img = cv2.threshold(img, 75, 255, cv2.THRESH_BINARY) # targetIMG, 임계값, 최대값, 인수
# cv2.imshow("sample", my_img)
# cv2.waitKey(0)

"""마스킹"""
# mask = cv2.imread("D:/python/python-study/img/masking.png", 0) # 채널수(색상에 대한 정보를 담아두는 곳)가 1인 이미지로 변환
# mask = cv2.resize(mask, (img.shape[1], img.shape[0]))
# my_img = cv2.bitwise_and(img, img, mask=mask)
# cv2.imshow("sample", my_img)
# cv2.waitKey(0)

"""흐림"""
# my_img = cv2.GaussianBlur(img, (5, 5,), 0)
# cv2.imshow("sample", my_img)
# cv2.waitKey(0)

"""노이즈 제거"""
# my_img = cv2.fastNlMeansDenoisingColored(img)
# cv2.imshow("sample", my_img)
# cv2.waitKey(0)

"""팽창"""
# filt = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], np.uint8)
# my_img = cv2.dilate(img, filt)
# cv2.imshow("sample", my_img)
# cv2.waitKey(0)

"""침식"""
# filt = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], np.uint8)
# my_img = cv2.erode(img, filt)
# cv2.imshow("sample", my_img)
# cv2.waitKey(0)


"""데이터 부풀리기"""
def scratch_image(img, flip=True, thr=True, filt=True, resize=True, erode=True):
    methods = [flip, thr, filt, resize, erode]
    img_size = img.shape # 이미지 사이즈
    filter1 = np.ones((3, 3))

    images = [img]

    scratch = np.array([
        lambda x: cv2.flip(x, 1),  # 회전
        lambda x: cv2.threshold(x, 100, 255, cv2.THRESH_TOZERO)[1],  # 임계값 처리
        lambda x: cv2.GaussianBlur(x, (5, 5), 0),  # 흐림
        lambda x: cv2.resize(cv2.resize(
            x, (img_size[1] // 5, img_size[0] // 5)), (img_size[1], img_size[0])),  # 리사이즈
        lambda x: cv2.erode(x, filter1)  # 침식

    ])

    doubling_images = lambda f, img: np.r_[img, [f(i) for i in img]]

    for func in scratch[methods]:
        images = doubling_images(func, images)

    return images


scratch_image = scratch_image(img)

if not os.path.exists("scratch_images"):
    os.mkdir("scratch_images")
for num, im in enumerate(scratch_image):
    cv2.imwrite("scratch_images/" + str(num) + ".png", im)
