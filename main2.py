# import turtle
# import turtle as t
# import random
#
#
# # x = turtle.Turtle()
# # x.speed(0)
# # x.left(180)
# t.speed(0)
# count = 0
# t.bgcolor('black')
# dicti = ('red', 'green', 'blue', 'cyan')
#
# for i in range(1000):
#     t.color(dicti[i % 4])
#     t.forward(0+i)
#     t.right(91)
#     t.dot()
#     # x.forward(5 + i)
#     # x.right(89)
#     # x.color(dicti[i % 4])
#
# t.mainloop()
#
# # a, b = map(int, input().split())
# # c, c1, count,  = 0, 0, 1,
# #
# # while any([not c, not c1]):
# #     if a >= b and not c:
# #         c = count
# #     if total >= 1000000 and not c1:
# #         c1 = count
# #     a *= 3
# #     total += a
# #     count += 1
# #
# # print(c, c1)
#
# # a = 'str'
# # all([
# #     isinstance(a, int),
# #     a > 0
# # ]) #True False
# #
# # if c > 0 or count+'str' or c1 == 0 or False:
# #     pass
#
#
# # d = a + k**(n-1)*a
#
# # print(sum(map(int, filter(lambda x: x if x.isdigit() else False, input().split()))))
#
# # lst = input().split()
# # total = 0
#
# # for item in lst:
# #     try:
# #         item = int(item)
# #         total += item
# #     except:
# #         try:
# #             item = float(item)
# #             total += item
# #         except:
# #             continue
# #
# # print(total)
import random
import datetime
import time
from math import factorial

# # 1 задание
#
# n = int(input())
# print(*(f'{n} * {i} = {n*i}' for i in range(1, 10)), sep='\n')

# 2 задание

# dictiVAL = ((1, 50, 0.5), (0.02, 1, 0.01), (2, 100, 1))
# dicti = {
#     'dol': 0,
#     'rub': 1,
#     'eur': 2,
# }
# val1 = input('Введите вашу валюту\ndol\nrub\neur\n')
# val2 = input('Введите в какую валюту конвертировать\ndol\nrub\neur\n')
# total = int(input('Введите кол-во деняк\n'))
#
#
# print(dictiVAL[dicti[val1]][dicti[val2]]*total, val2)
#
# # 3 задание
#
# x, y = map(int, input().split())
#
# while True:
#     num = int(input())
#     if x <= num <= y:
#         for i in range(x, y+1):
#             print(i, end=' ') if i != num else print(f'!{num}!', end=' ')
#         break

# 4 задание

# flag, count, start, x = True, 0, time.perf_counter(), random.randint(1, 500)
#
# while flag:
#     count += 1
#     num = int(input())
#     if num > x:
#         print('Меньше')
#     elif num < x and num:
#         print('Больше')
#     elif num == x:
#         print('Вы выиграли')
#         end = time.perf_counter()
#         print(f'Вы использовали {count} попыток')
#         print(f'Вы потратили {end-start} секунд')
#         flag = False
#     elif not num:
#         print('Спасибо за игру')
#         flag = False

# # 1 задание
# lst = tuple(i for i in range(int(input()), int(input())+1))
# print(sum(lst), sum(lst)/(len(lst)))
#
# # 2 задание
#
# print(factorial(int(input())))
#
# # 3 задание
#
# print('*' * int(input()), sep='')
#
# # 4 задание
#
# print(int(input()) * input(), sep='')


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(3))

