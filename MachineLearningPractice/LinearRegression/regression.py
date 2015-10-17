# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:56:03 2015

@author: liuxiangyu
"""
from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t'))-1
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat
    
def standRegres(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws

def lwlr(testPoint, xArr, yArr, k = 1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
#    eye()返回一个对角线元素为1，其他元素为0的二维数组。 
    weights = mat(eye((m)))
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat

def ridgeRegres(xMat, yMat, lam=0.2):
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * lam
    if linalg.det(denom) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = denom.I * (xMat.T*yMat)
    return ws

def ridgeTest(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    yMean = mean(yMat,0)
    yMat = yMat - yMean
    xMeans = mean(xMat,0)
    xVar = var(xMat,0)
    xMat = (xMat - xMeans)/xVar
    numTestPts = 30
    wMat = zeros((numTestPts,shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat, yMat, exp(i-10))
        wMat[i:] = ws.T
    return wMat

def rssError(yArr,yHatArr):
    return ((yArr - yHatArr)**2).sum()

if __name__ == '__main__':
#    xArr,yArr=loadDataSet('ex0.txt')
#    print xArr[0:2]
#    ws = standRegres(xArr,yArr)
#    print ws
#    xMat = mat(xArr)
#    yMat = mat(yArr)
#    yHat = xMat*ws
#    fig = plt.figure()
#    ax = fig.add_subplot(111)
#    ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])
#    xCopy = xMat.copy()
#    xCopy.sort(0)
#    yHat=xCopy*ws
#    ax.plot(xCopy[:,1], yHat)
#    plt.show()
    
#==============================================================================
#     Relatigity between Estimate and Actual
#==============================================================================
#    print corrcoef(yHat.T, yMat)
    
#==============================================================================
#     Locally Weighted Linear Regression
#==============================================================================
#    print yArr[0]
#    print lwlr(xArr[0],xArr,yArr,1.0)
#    print lwlr(xArr[0],xArr,yArr,0.001)
    
#    yHat = lwlrTest(xArr,xArr,yArr,1.0)
#    yHat = lwlrTest(xArr,xArr,yArr,0.01)
#    yHat = lwlrTest(xArr,xArr,yArr,0.003)
#    xMat = mat(xArr)
#    srtInd = xMat[:,1].argsort(0)
#    xSort = xMat[srtInd][:,0,:]
#    fig = plt.figure()
#    ax = fig.add_subplot(111)
#    ax.plot(xSort[:,1],yHat[srtInd])
#    ax.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0], s = 2, c = 'red')
#    plt.show()
    
#==============================================================================
#     Predict abalone's age
#==============================================================================
    abX,abY=loadDataSet('abalone.txt')
#    yHat01=lwlrTest(abX[0:99],abX[0:99],abY[0:99],0.1)
#    yHat1=lwlrTest(abX[0:99],abX[0:99],abY[0:99],1)
#    yHat10=lwlrTest(abX[0:99],abX[0:99],abY[0:99],10)
    
#    为了分析预测误差大小，可以调用rssError()计算出这一指标
#    print rssError(abY[0:99],yHat01.T)
#    print rssError(abY[0:99],yHat1.T)
#    print rssError(abY[0:99],yHat10.T)
    
#==============================================================================
#     可以看出，使用较小的核将得到较低的误差。那么为什么不在所有数据集上都使用最小的核呢？
#     因为使用最小的核将造成过拟合，对新数据不一定能达到最好的预测效果。
#     下面来看看它们在新数据上的表现
#==============================================================================
#    yHat01=lwlrTest(abX[100:199],abX[0:99],abY[0:99],0.1)
#    yHat1=lwlrTest(abX[100:199],abX[0:99],abY[0:99],1)
#    yHat10=lwlrTest(abX[100:199],abX[0:99],abY[0:99],10)
    
#    print rssError(abY[100:199],yHat01.T)
#    print rssError(abY[100:199],yHat1.T)
#    print rssError(abY[100:199],yHat10.T)
    
#==============================================================================
#     在上面三个参数中，核大小等于10时的测试误差最小，但它在训练集上的误差却是最大的。
#     接下来再和简单线性回归做比较：
#==============================================================================
    
#    ws = standRegres(abX[0:99],abY[0:99])
#    yHat = mat(abX[100:199]) * ws
#    print rssError(abY[100:199],yHat.T.A)
    
#    简单线性回归达到了与局部加权线性回归类似的效果。
    
#==============================================================================
#     Ridge Regression
#==============================================================================
    
    ridgeWeights = ridgeTest(abX, abY)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ridgeWeights)
    plt.show()