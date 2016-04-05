#!/usr/bin/env python
# -*- coding:utf-8 -*-

import fractions

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def genFactorial(start=0):
    n = 1
    c = 1
    for i in enumerate(range(start)):
        n *= i
        c += 1
    while True:
        yield n
        n *= c
        c += 1

def genCollatz(n):
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        yield n

# totient function (euler's phi function)
def phi(n):
    return len([i for i in range(n) if fractions.gcd(i, n) == 1])


def ispandigital(s):
    # if isinstance(s, int):
    #     s = str(s)
    n = len(s)
    if n > 9:
        return False
    s = sorted(s)
    if s[0] != '1':
        return False
    for i in range(1, len(s)):
        if int(s[i]) - int(s[i-1]) != 1:
            return False
    return True
