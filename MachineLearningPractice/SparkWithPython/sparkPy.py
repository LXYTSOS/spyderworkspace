# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:01:18 2015

@author: liuxiangyu
"""
import os
from pyspark import SparkContext
import matplotlib.pyplot as plt

# Configure the environment
if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME'] = '/Users/software/spark/spark-1.5.0-bin-hadoop2.6'
 
# Create a variable for our root path
SPARK_HOME = os.environ['SPARK_HOME']

sc = SparkContext("local[2]", "SparkWithPython")

user_data = sc.textFile("u.user")
print user_data.first()

user_fields = user_data.map(lambda line: line.split("|"))
num_users = user_fields.map(lambda fields: fields[0]).count()
num_genders = user_fields.map(lambda fields: fields[2]).distinct().count()
num_occupations = user_fields.map(lambda fields: fields[3]).distinct().count()
num_zipcodes = user_fields.map(lambda fields: fields[4]).distinct().count()
print "Users: %d, genders: %d, occupations: %d, ZIP codes: %d" % \
(num_users, num_genders, num_occupations, num_zipcodes)

#使用matplotlib的hist函数创建一个直方图，分析用户年龄的分布情况

ages = user_fields.map(lambda x: int(x[1])).collect()
plt.hist(ages, bins=20, color='lightblue', normed=True)
fig = plt.gcf()
fig.set_size_inches(8, 5)
