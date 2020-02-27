#! /usr/bin/env python
# -*- coding: utf-8 -*-
# list_my =[ i for i in range(2,30)]
def coundown(x):
    if x == 0:
        return
    else:
        print('Hello world')
        coundown(x-1)
coundown(3)