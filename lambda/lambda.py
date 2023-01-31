import re

"""람다 기초"""
# a = 4
# def test(a):
#     return 2 * a ** 2 - 3 * a + 1
#
#
# test2 = lambda a: 2 * a ** 2 - 3 * a + 1
#
# print(test(3))
# print(test2(3))

"""람다에 의한 계산"""
# x = 5
# y = 6
# z = 2
# def test(x, y, z):
#     return x*y + z
#
# test2 = lambda x, y, z: x*y + z
# print(test(1, 3, 5))
# print(test2(1, 3, 5))

"""IF를 이용한 람다"""
# a1 = 13
# a2 = 32
#
# test = lambda x: x**2 - 40*x + 350 if 10 <= x < 30 else 50
#
# print(test(15))

"""리스트 분할"""
# test_sentence = "this is a test sentence"
#
# test2 = test_sentence.split(" ")
# print(test2[4])

"""리스트 여러 기호로 분한"""
# test_sentence = "2023.01.31 20:26"
# test3 = re.split("[. : ]", test_sentence)
# print(test3)

"""고차함수(map)"""
# a = [1, 3, 5, -6, 5]
# test = list(map(abs, a)) # list(map(함수, 배열))
#
# time_list = [
#     "2006/11/26_2:40",
#     "2009/1/16_23:35",
#     "2014/5/4_14:26",
#     "2017/8/9_7:5",
#     "2020/1/5_22:15"
# ]
#
# get_hour = lambda x: int(re.split("[/ _ :  ]", x)[3])
# hour_list = list(map(get_hour, time_list))
# print(hour_list)

"""filter"""
# time_list = [
#     "2006/11/26_2:40",
#     "2009/1/16_23:35",
#     "2014/5/4_14:26",
#     "2017/8/9_7:5",
#     "2020/1/5_22:15"
# ]
#
# is_first_half = lambda x: int(re.split("[/_:]", x)[1]) - 7 < 0
# first_half_list = list(filter(is_first_half, time_list))
# print(first_half_list)

"""sorted"""
# nest_list = [
#     [2006, 11, 26, 2, 40],
#     [2009, 1, 16, 23, 35],
#     [2014, 5, 3, 23, 65],
#     [2020, 7, 4, 24, 78],
# ]
#
# sort_by_time = sorted(nest_list, key=lambda x: x[3])
# print(sort_by_time)

