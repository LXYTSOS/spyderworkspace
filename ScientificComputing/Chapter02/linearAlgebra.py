# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 20:07:55 2016

@author: liuxiangyu
"""

import numpy as np

a = np.matrix([[1,2,3],[5,5,6],[7,9,9]])
b = a*a**-1
print b

a = np.array([1,2,3])
print a.reshape((-1,1))
print a.reshape((1,-1))