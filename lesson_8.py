# -*- coding: utf-8 -*-
import random
from math import sqrt
import time
import requests

#1
value = 777
slot = 'Win' if value == 777 else 'Loss'
print(slot)

#Генератор выводит список простых чисел
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print([x for x in range(101) if is_prime(x)])

#2
def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper
@decorator_function
def hello_world():
    print('Hello world!')
hello_world()

#3
def timemometr(f):
    from time import time
    def wrapper(*args):
        start_time = time()
        value = f(*args)
        end_time = time()
        print('Function execution time', end_time - start_time, ' sec.')
        return value
    return wrapper

@timemometr
def requests_example(url):
    webpage = requests.get(url)
    return webpage.text

url = 'https://google.com'
text = requests_example(url)
print(text)

#4
n = 1000000
@timemometr
def gen_n(n):
    gen_n = [x for x in range(n)]
    return gen_n
@timemometr
def lst(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst

print('Generator time:')
gen_n(n)
print('List time:')
lst(n)


