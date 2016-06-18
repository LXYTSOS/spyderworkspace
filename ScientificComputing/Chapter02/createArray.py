# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 22:06:35 2016

@author: liuxiangyu
"""

import numpy as np

#等差数组［0，1），步长0.1
a = np.arange(0,1,0.1)
print a

#开始结束值，个数，步长1/9
b = np.linspace(0,1,10)
print b

#步长1/10
c = np.linspace(0,1,10,endpoint=False)
print c

#等比数列，0是10^0,2表示10^2
d = np.logspace(0,2,5)
print d

#基数可以通过base参数指定，默认值为10，创建一个比例为2^(1/12)等比数组
e = np.logspace(0,1,12,base=2,endpoint=False)
#此等比数组的比值是音乐中相差半音的两个音阶之间的频率比值，因此可以用它计算一个八度中所有半音的频率
print e