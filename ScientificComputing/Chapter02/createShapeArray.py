# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 22:39:09 2016

@author: liuxiangyu
"""

import numpy as np

#empty()仅仅分配数组所使用的内存，不对数组元素进行初始化操作，因此它的运行速度是最快的
a = np.empty((2,3),np.int)
print a

b = np.zeros(4,np.float)
print b

#zeros_like(),ones_like(),empty_like()等函数可以创建与参数数组的形状及类型相同的数组

#从函数中创建
def func(i):
    return i%4+1

c = np.fromfunction(func,(10,))
print c

def func2(i,j):
    return (i+1) * (j+1)

d = np.fromfunction(func2,(9,9))
print d