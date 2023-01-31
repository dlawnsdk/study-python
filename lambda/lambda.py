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
a1 = 13
a2 = 32

test = lambda x: x**2 - 40*x + 350 if 10 <= x < 30 else 50

print(test(15))