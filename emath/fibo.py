#!/usr/bin/env python
# -*- coding:utf-8 -*-

def genFibo():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b
