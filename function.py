#! /usr/bin/env python
# -*- coding: utf-8 -*-

def benchmark(func):
    import time

    # def wrapper():
    #     start = time.time()
    #     func()
    #     end = time.time()
    #     print(f'[*] Время выполнения: {end - start} секунд.')
    #
    # return wrapper

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'[*] Время выполнения: {end - start} секунд.')
        return return_value

    return wrapper


# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')


# fetch_webpage()
# @benchmark
def multipli(*args):
    # for ar in args:
    return pow(args)

foo = (98, 3, 2)
print(multipli(foo))
