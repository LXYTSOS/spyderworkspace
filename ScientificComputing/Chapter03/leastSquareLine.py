# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 22:15:08 2016

@author: liuxiangyu
"""

import numpy as np
from scipy.optimize import leastsq

X = np.array([8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78])
Y = np.array([7.01, 2.78, 6.47, 6.71, 4.7, 4.23, 4.05])
#print zip(X, Y)

def residuals(p):
    "计算以p为参数的直线和原始数据之间的误差"
    k,b=p
    return Y - (k*X + b)

#leastsq使得residuals()的输出数组的平方和最小，参数的初始值为[1,0]
r = leastsq(residuals,[1,0])
k,b = r[0]
print "k = ",k,"b = ",b

def S(k, b):
    "计算直线y=k*x+b和原始数据X、Y的误差平方和"
    error = np.zeros(k.shape)
    for x, y in zip(X, Y):
        error += (y - (k*x +b))**2
    return error