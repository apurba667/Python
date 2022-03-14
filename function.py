# def f():
#     print("hello!")
#
#
# def f1(a, b):
#     return a + b
#
#
# def name(name):
#     print("Your name is " + name)
#
#
# nam = input("Enter your name!\n")
#
# name(nam)

# def fibonacci(n):
#     if n == 0:
#         return 0
#     else:
#         x = 0
#         y = 1
#         print(x)
#         print(y)
#
#         for i in range(1,n):
#             z = x+y
#             x = y
#             y = z
#             print(z)
#
# fibonacci(8)

import random as r
secret_age = r.randint(1,10)
flag = False

def game_func(gussed_age, secret):
    if gussed_age < secret:
        return 'Too high'
    elif gussed_age > secret:
        return 'Too low'
    else:
        return 'Correct!'


for i in range(1,6):
    print('Take a guess. you have '+str(6-i)+' guesses left ' )
    guess = input()
    if game_func(int(guess),secret_age) == 'Correct':
        print('You won the game!')
        flag = True
        break

if not flag:
    print('You loose the game! ')