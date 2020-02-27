#! /usr/bin/env python
# -*- coding: utf-8 -*-
# easy_unpack = (1, "h")
# easy_unpack2 = [1, 2, 3, 4, 5, 6, 7, 9]
# print(easy_unpack.__sizeof__())
# print(easy_unpack2.__sizeof__())
# print(easy_unpack.count(10))
# print(easy_unpack.index(10))
def checkio(array):
	"""
        sums even-indexes elements and multiply at the last
    """
	promej = []
	for i in array:
		if i % 2 == 0:
			promej.append(i)
		else:
			continue
	print(sum(promej) * array[-1])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	print('Example:')
	print(checkio([0, 1, 2, 3, 4, 5]))

	assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
	assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
	assert checkio([6]) == 36, "(6)*6=36"
	assert checkio([]) == 0, "An empty array = 0"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")