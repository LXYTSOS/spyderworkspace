# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 19:36:49 2016

@author: liuxiangyu
"""

import numpy as np
from scipy import interpolate
import pylab as pl

x1 = np.linspace(0,10,20)
y1 = np.sin(x1)
sx1 = np.linspace(0,12,100)
sy1 = interpolate.UnivariateSpline(x1,y1,s=0)(sx1)
#pl.plot(x1,y1,'ro')
#pl.plot(sx1,sy1,label=str("spline"))

x2 = np.linspace(0,20,200)
y2 = np.sin(x2) + np.random.standard_normal(len(x2))*0.2
sx2 = np.linspace(0,20,2000)
yx2 = interpolate.UnivariateSpline(x2,y2,s=8)(sx2)
pl.plot(x2,y2,'ro')
pl.plot(x2,np.sin(x2),label=str("spline"))
pl.plot(x2,y2,label=str("spline"))
pl.legend(loc='lower right')

pl.show()