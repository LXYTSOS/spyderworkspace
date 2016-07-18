# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 22:27:20 2016

@author: liuxiangyu
"""
import numpy as np
persontype = np.dtype({
    'names':['name', 'age', 'weight'],
    'formats':['S32', 'i', 'f']
}, align=True)

a = np.array([("Zhang",32,75.5), ("Wang", 24, 65.2)], dtype=persontype)

print a.dtype
print a[0]
print a[0].dtype
print a[0]["name"]

c = a[1]
c["name"] = "Li"
print a[1]["name"]

b = a["age"]
print b
b[0] = 40
print a[0]["age"]
a.tofile("test.bin")