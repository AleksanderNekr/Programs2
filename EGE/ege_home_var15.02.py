import string

# from itertools import product
# for x, y, z, w in product(range(2), range(2), range(2), range(2)):
#     if (not x != y) or (y and (not z)) or (z and (not w)) is False:
#         print(w, z, y, x)

# # for s1 in range(10, 100):
# #     s = s1
# #     s = (s+1) // 7
# #     n = 36
# #     while s < 2050:
# #         s = s * 2
# #         n = n + 3
# #     if n == 60:
# #         print(s1, '!OOOO!')
# name = 'ТИМОФЕЙ'
# counter = 0
# for a, b, c, d, e in product(name, name, name, name, name):
#     wor = a + b + c + d + e
#     if wor.count('Т') >= 1 and wor.count('Й') <= 1:
#         counter += 1
#         # print(wor)
# print(counter)

# s = '0'
# num = int('1' * 85)
# while True:
#     num += 1
#     num4 = d(num)
#     num4 = num4.replace('0', '1')
#     s1 = s + num4
#     while '01' in s1 or '02' in s1 or '03' in s1:
#         s1 = s1.replace('01', '30')
#         s1 = s1.replace('02', '101')
#         s1 = s1.replace('03', '202')
#     if s1.count('1') == 15 and s1.count('2') == 10:
#         if s1.count('3') == 60:
#             print(s.count('1'))
#             exit(1)

# a = int(input())
# b = int(input())
# print(d(a))


# def number_system(num):
#     ans = ''
#     strin = '0123456789' + string.ascii_uppercase
#     while num > 0:
#         num, index = divmod(num, 7)
#         ans = strin[index] + ans
#     return ans


# for x in range(10000):
#     if number_system(7 ** 15 + 7 ** 3 - 1 - x).count('6') == 12:
#         print(x)
#         break

# for A in range(1, 1001):
#     count = 0
#     for x in range(1, 1001):
#         if 70 % A == 0:
#             if x % 28 != 0 or x % A == 0 or x % 21 != 0:
#                 count += 1
#     if count == 1000:
#         print(A)


# def F(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 2 == 0:
#         return F(n / 2)
#     if n % 2 != 0:
#         return 1 + F(n - 1)


# for n in range(10000):
#     if F(n) == 12:
#         print(n)
#         break


# def IfCountOfDelMore17(number):
#     count = 0
#     for i in range(1, number + 1):
#         if number % i == 0:
#             count += 1
#             if count > 17:
#                 return True
#     return False


# count = 0
# ans = 0
# for i in range(10001, 50001):
#     if IfCountOfDelMore17(i):
#         count += 1
#         if count == 1:
#             ans = i

# print(count, ans)

for x1 in range(1000):
    m = 0
    s = 0
    x = x1
    while x > 0:
        d = x % 8
        s += d
        if d > m:
            m = d
        x = x // 8
    if m == 5 and s == 12:
        print(x1)
        print("I'm back again and forever!")
        break
