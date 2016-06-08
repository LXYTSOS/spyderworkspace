# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:25:54 2016

@author: liuxiangyu
"""

import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.array([[1, 2, 3, 4],[4, 5, 6, 7],[7, 8, 9, 10]])
print b
print a.shape
print c.shape
print c
c.shape = 4,3
print c
c.shape = 2,-1
print c

d = a.reshape(2,2)
print d
print a

#数组a和d共享了数据存储空间，因此修改其中任意一个数组的元素都会同时修改另外一个数组的内容
a[1] = 100
print a
print d

#数组的元素类型可以通过dtype属性获得
print c.dtype

#可以通过dtype参数在创建数组时指定元素类型，float时64位双精度浮点类型，
#complex时128位双精度复数类型
arrFloat = np.array([1,2,3,4], dtype=np.float)
print arrFloat
print arrFloat.dtype
arrComplex = np.array([1,2,3,4], dtype=np.complex)
print arrComplex
print arrComplex.dtype