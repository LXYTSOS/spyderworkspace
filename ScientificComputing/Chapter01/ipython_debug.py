# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 22:41:34 2016

@author: liuxiangyu
"""

import pylab as pl
import numpy as np

def test_debug():
    x = np.linspace(1, 50, 10000)
    img = np.sin(x*np.cos(x))
    img.shape = 100, -1
    pl.imshow(img)
    pl.show

test_debug()