# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:52:50 2015

@author: sl169
"""

from numpy import *

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine)
        dataMat.append(fltLine)
    return dataMat

def binSplitDataSet(dataSet, feature, value):
    mat0 = dataSet[nonzero(dataSet[:, feature] > value)[0],:][0]
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0],:][0]
    return mat0, mat1

#def createTree(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):
#    feat, val = chooseBestSplit(dataSet, leafType, errType, ops)
#    if feat == None: return val
#    retTree = {}
#    retTree['spInd'] = feat
#    retTree['spVal'] = val
#    lSet, rSet = binSplitDataSet(dataSet, feat, val)
#    retTree['left'] = createTree(lSet, leafType, errType, ops)
#    retTree['right'] = createTree(rSet, leafType, errType, ops)
#    return retTree

if __name__ == '__main__':
    testMat = mat(eye(4))
    print testMat
    mat0, mat1 = binSplitDataSet(testMat, 1,0.5)
    print mat0
    print mat1