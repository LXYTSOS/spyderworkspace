# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 23:46:32 2016

@author: liuxiangyu
"""

import numpy as np
a = np.arange(0,60,10).reshape(-1,1) + np.arange(0,6)
print a[2::2,::2]