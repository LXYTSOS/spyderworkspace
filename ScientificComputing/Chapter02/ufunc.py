# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 23:16:13 2016

@author: liuxiangyu
"""

import numpy as np

#x = np.linspace(0,2*np.pi,10)
#等差数列
#y = np.sin(x)
#print y

#可以通过out参数指定计算结果的保存位置
#t = np.sin(x, out=x)
#print t
#print x
#ufunc函数的返回值仍然是计算的结果，只不过它就是数组x，因此两个数组id是相同的
#print id(t) == id(x)

#比较np.sin和Python标准库中math.sin的速度

import time
import math
import numpy as np

x = [i * 0.001 for i in xrange(1000000)]
start = time.clock()
#enumerate函数用于遍历序列中元素的下标以及值
#for i, t in enumerate(x):
#    x[i] = math.sin(t)

#列表推导式
x = [math.sin(t) for f in x]
print "math.sin:", time.clock() - start

x = [i * 0.001 for i in xrange(1000000)]
x = np.array(x)
start = time.clock()
np.sin(x,x)
print "numpy.sin:", time.clock() - start

x = [i * 0.001 for i in xrange(1000000)]
start = time.clock()
for i, t in enumerate(x):
    x[i] = np.sin(t)

print "numpy.sin loop:", time.clock() - start