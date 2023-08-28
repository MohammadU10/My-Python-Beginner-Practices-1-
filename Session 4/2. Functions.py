
# 1. a Function for Average of Scores :

# def mean(L):
#     t = 0
#     for s in L:
#         t += s
#     return t / len(L)
#
#
# L = [16, 20]
# O = [12, 23, 53, 56]
#
# ml = mean(L)
# mo = mean(O)
#
# if ml > mo:
#     print("L is bigger than O")
# else:
#     print("O is bigger than L")


# 2. a Funtion for ghadre motlagh :
# def abs(x):
#     if x < 0:
#         x = x * -1
#     return x
#
# print(abs(-9))


# 3. a Funtion can be called through itself (تابع بازگشتی):
# def fib(N):
#     if N == 1:
#         return 1
#     if N == 2:
#         return 1
#     return fib(N-1) + fib(N-2)
#
# n = 1
# while True:
#     print(fib(n))
#     n += 1


# 4. a Function that Returns 2 Values :
# def minmax(L):
#     return min(L), max(L)
#
# P = [23, 345, 10, 234, 2000]
#
# minP, maxP = minmax(P)
#
# print(minP)
# print(maxP)
#
# print(minmax(P)[1])


# turtle() Method :
# import turtle as t
# t.speed(0)
#
# def sq():
#     for i in range(4):
#         t.fd(100)
#         t.left(90)
#
# sq()
# t.fd(200)
# sq()
# t.done()
#
# t.write("Welcome")
# t.done()

# turtle With random Function :
import turtle as t
import random as rd

t.speed(0)

def sq():
    for i in range(4):
        t.fd(100)
        t.left(90)

# sq(600)
t.pensize(5)
t.color("Red")
t.shape("circle")
t.pd()
t.penup()
for i in range(10):
    t.goto(rd.randint(-150, 150), 300)
    t.goto(0, 0)

t.done()