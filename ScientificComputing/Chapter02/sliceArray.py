# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 23:27:32 2016

@author: liuxiangyu
"""

import numpy as np
a = np.arange(10)
print a
print a[:-1]
a[2:4]=100,101
print a
print a[5:1:-2]

x = np.random.rand(10)
#产生一个长度为10，元素值为0到1的随机数组
print x
print x>0.5
print x[x>0.5]