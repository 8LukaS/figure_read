#! /usr/bin/env python
# -*- coding: utf-8 -*-
products = ['зубные щетки', 'расчески', 'заколки', 'бигуди для волос', 'парики', 'шиньоны',
    'ткани', 'ленты', 'тесьма', 'кружево', 'провода', 'шнуры', 'кабели',
    'линолеум', 'пленка', 'ковровые покрытия', 'мебельные гарнитуры',
    'автомобили', 'мотовелотовары', 'прицепы', 'книги', 'брошюры', 'альбомы',
    'картографические издания', 'нотные издания', 'листовые изоиздания',
    'календари', 'буклеты']

def binary_serch(products,item):
    low = 0
    high = len(products )-1
    while low <= high:
        mid =(low + high) // 2
        guess = products[mid]
        if guess == item:
            return mid
        else:
            low = mid + 1
    return None
print(binary_serch(products,'картографические издания'))
print('Длина списка:',len(products))

# "срезаем" первые десять элементов
# first_page = products[:10]

# начинаем с элемента с индексом 10, заканчиваем элементом с индексом 19
# second_page = products[10:20]
#
# # "-10" означает "десятый с конца"
# last_page = products[-10:]
#
# print('first_page:',second_page)
# print('second_page',last_page)
