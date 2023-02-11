import re
from collections import defaultdict
from collections import Counter
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

"""리스트 내포"""
# a = [1, -2, 3, -4, 5]
# print([abs(x) for x in a])
# b = [1, -2, 3, -4, 5]
# print(list(map(abs, b)))
# minute_data = [30, 155, 180, 74, 11, 60, 82]
# h_m_split = lambda x: [x // 60, x % 60]
# h_m_data = [h_m_split(x) for x in minute_data]
# print(h_m_data)
# minute_data: list = [30, 155, 180, 74, 11, 60, 82]
# print([a for a in minute_data if a % 60 == 0])

"""여러 배열 동시에 루프시키기"""
# a = [1, -2, 3, -4, 5]
# b = [5, 2, -6, 3, -8]
# for x, y in zip(a, b):
#     print(x, y)
# print([x**2 + y**2 for x, y in zip(a, b)])

# hour = [0, 2, 3, 1, 0, 1, 1]
# minute = [30, 35, 0, 14, 11, 0, 22]
# h_m_combine = lambda x, y: x*60 + y
# minute_data1 = [h_m_combine(x, y) for x, y in zip(hour, minute)]
# print(minute_data1)

"""딕셔너리"""
# d = {}
# list = ["poo", "boo", "pop", "poo"]
# for key in list:
#     print(key)
#     if key in d:
#         d[key] += 1
#     else:
#         d[key] = 1
# print(d)

# d = defaultdict(int)
# lst = ["foo", "poo", "pop", "foo", "bob", "pop"]
# for key in lst:
#     d[key] += 1
# print(d)

# description = "Artificial intelligence (AI, also machine intelligence, MI) is " \
#     "intelligence exhibited by machines, rather than " \
#     "humans or other animals (natural intelligence, NI)."
#
# char_freq = defaultdict(int)
#
# for i in description:
#     # print(i)
#     char_freq[i] += 1
# print(sorted(char_freq.items(), key=lambda x: x[1], reverse=True)[:5])

# d = {}
# price = [
#     ("apple", 50),
#     ("banana", 120),
#     ("grape", 500),
#     ("apple", 70),
#     ("lemon", 150),
#     ("grape", 1000)
# ]
#
# for key, value in price:
#     if key in d:
#         d[key].append(value)
#     else:
#         d[key] = [value]
#     print(d)

# d = defaultdict(list)
# price = [
#     ("apple", 50),
#     ("banana", 120),
#     ("grape", 500),
#     ("apple", 70),
#     ("lemon", 150),
#     ("grape", 1000)
# ]
#
# for key, value in price:
#     d[key].append(value)
# print([sum(x) / len(x) for x in d.values()]) # 리스트 내포

"""Counter"""
# lst = ["foo", "bar", "pop", "pop", "foo", "popo"]
# d = Counter(lst)
# print(d.keys())

# d = Counter("A counter is a dict subClass for counting hashable objects")
#
# print(d.most_common(5))

# description = "" \
#               "Artifical intelligence (AI, also machine intelligencem MI is" \
#               "intelligence exhibited by machines, rather than" \
#               "humans or other animals (nature intelligence, NI)"
#
# d = Counter(description)
# print(d.most_common(10))

"""연습문제"""
# a = 8
# basic = lambda x: x * 5  if x < 8 else a // 2
# print("계산 결과")
# print(basic(a))
import re
from collections import defaultdict
from collections import Counter
# time_list = [
#     "2018/1/23_19:40",
#     "2016/5/7_5:25",
#     "2018/8/21_10:50",
#     "2017/8/9_7:5",
#     "2015/4/1_22:15"
# ]
#
# get_month = lambda x: int(re.split("[/_:]", x)[0])
# month_list = list(map(get_month, time_list))
# length = [3, 1, 6, 2, 8, 2, 9]
# side = [4, 1, 15, 18, 7, 2, 19]
# height = [10, 15, 17, 13, 11, 19, 18]
# volume = [x * y * z for x, y, z in zip(length, side, height)]

price = [
    ("strawberry", 520),
    ("pear", 200),
    ("peach", 400),
    ("apple", 170),
    ("lemon", 150),
    ("grape", 1000),
    ("strawberry", 750),
    ("pear", 400),
    ("strawberry", 500),
    ("lemon", 300),
    ("strawberry", 700)
]

d = defaultdict(list)
price_key_count = []
for key, value in price:
    d[key].append(value)
    price_key_count.append(key)
print([sum(x) / len(x) for x in d.values()])
