# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 22:30:11 2016

@author: liuxiangyu
"""

import numpy as np
from scipy import signal
import pylab as pl

t = np.linspace(0, 10, 1000)
x = signal.chirp(t, 5, 10, 30)
pl.plot(t, x)
#pl.show()
#print x[:5]
#设置曲线颜色为红色
pl.gca().lines[0].set_color("r")
pl.draw