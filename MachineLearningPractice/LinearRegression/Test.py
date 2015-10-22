# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:04:41 2015

@author: sl169
"""

from numpy import *

#question about regresion formula, why when transpose xMat, we still need to
#translate mat(yArr)
#This is what happend to xArr
a = [[1,2,3],[4,5,6],[7,8,9]]
#And this is what happend to yArr
b = [1,2,3]
#So When transfer xArr to matrix, it will be 3*3
m = mat(a)
#While transger yArr to matrix, it is 1*3
#So when we mutiply xMat with yMat, We must transpose yMat to 3*1
#Then it is xMat * yMat.T
n = mat(b).T
#print m*n

#mMean = mean(m,0)
#print mMean

mVar = var(m,0)
print mVar