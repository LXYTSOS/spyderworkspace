# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 19:06:40 2016

@author: liuxiangyu
"""

from scipy.optimize import fsolve
from math import sin

def f(x):
    x0, x1, x2 = x.tolist()
    return[
        5*x1+3,
        4*x0*x0 - 2*sin(x1*x2),
        x1*x2 - 1.5
    ]

#f计算方程组的误差，[1,1,1]是未知数的初始值
result = fsolve(f, [1,1,1])
print result
print f(result)