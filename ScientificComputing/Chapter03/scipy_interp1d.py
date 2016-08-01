# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 19:20:03 2016

@author: liuxiangyu
"""

import numpy as np
from scipy import interpolate
import pylab as pl

x = np.linspace(0,10,11)
y = np.sin(x)

xnew = np.linspace(0,10,101)
pl.plot(x,y,'ro')
for kind in ['nearest', 'zero', 'slinear', 'quadratic']:
    f = interpolate.interp1d(x,y,kind=kind)
    ynew = f(xnew)
    pl.plot(xnew,ynew,label=str(kind))

pl.legend(loc='lower right')
pl.show()