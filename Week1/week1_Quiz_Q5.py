#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:29:15 2019

@author: lyonce
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:14:02 2019

@author: lyonce
"""

from math import log

'''
a. 2 ^ (2 ^ n)
b. 2 ^ (n^2)
c. (n ^ 2) * log(n)
d. n 
e. n ^ (2^n)
dcbae
'''

def a(n):
    return 2**(2**n)

def b(n): 
    return 2**(n**2)

def c(n):
    return (n**2) * log(n, 2)

def d(n):
    return n

def e(n):
    return n**(2**n)

def order(n):
    return sorted((f(n), f.__name__) for f in [a, b, c, d, e])

def answer(ordering):
    return [f for x, f in ordering]

test = answer(order())
print(test)

