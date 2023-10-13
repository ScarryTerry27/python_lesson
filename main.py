# import math

# a, b = int(input()), int(input())
#
# print(f'P = {(a+b)*2}\nS = {a*b}')
#
# print(int(input())*math.pi)
#
# # 5
# print('V = ', (a:=int(input()))**3, '\nS = ', (a**2)*6)
#
# # 6
# a, b, c = (int(input()) for _ in range(3))
# print(f'V = {a*b*c}\nS = {2*(a*b+b*c+a*c)}')
#
# # 7
# r = int(input())
# print(f'L = {2*math.pi*r}\nS = {math.pi*(r**2)}')
#
# # 8
# a, b = int(input()), int(input())
# print(f'Среднее = {(a + b)/2}')
#
# # 9
# a, b = abs(int(input())), abs(int(input()))
# print(f'Среднее геометрическое = {(a*b)**0.5}')
#
# # 15
# s = int(input())
# R = (s/math.pi)**0.5
# print(f'L = {2*math.pi*R}')
# print(f'D = {2*R}')
#
# # 16
# x1, x2 = (int(input()) for _ in range(2))
# print(abs(x2-x1))
#
# # 17
#
# a, b, c = (int(input()) for _ in range(3))
# print(x1:=abs(a-c), x2:=abs(b-c), x1+x2, sep='\n')
#
# # 18
#
# a, b, c = (int(input()) for _ in range(3))
# print(abs(c-a)*abs(b-c))
#
# # 19
#
# x1, y1, x2, y2 = map(int, input().split())
# print(f'S = {abs(x2-x1)*abs(y2-y1)}\nP = {2*(abs(x2-x1)+abs(y2-y1))}')
#
# # 20
# x1, y1, x2, y2 = map(int, input().split())
# print(((x2-x1)**2 + (y2-y1)**2)**0.5)
#
# # 21
#
# x1, y1, x2, y2, x3, y3 = map(int, input().split())
# l1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
# l2 = ((x3-x1)**2 + (y3-y1)**2)**0.5
# l3 = ((x3-x2)**2 + (y3-y2)**2)**0.5
# P = l1 + l2 + l3
# p = P/2
# S = (p * (p - l1) * (p - l2) * (p - l3))**0.5
# print(f'P = {P}\nS = {S}')
#
# # 22
#
# a, b = int(input()), int(input())
# a, b = b, a

# def fib_1(n):
#     dicti = {1: 1, 2: 1}
#
#     def fib(n):
#         if n in dicti.keys():
#             return dicti[n]
#         else:
#             dicti[n] = fib(n-1) + fib(n-2)
#             return fib(n-1) + fib(n-2)
#
#     fib(n)
#     print(dicti)
#     return dicti[n]
#
#
# print(fib_1(7))
# print(fib_1(13))
a = 1
b = 1

if a > b:
    print('a больше b')
elif a == b:
    print('a равно b')
else:
    print('a меньше b')