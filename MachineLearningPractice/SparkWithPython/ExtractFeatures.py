# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:10:18 2015

@author: sl169
"""

#import os
from pyspark import SparkContext


def get_mapping(rdd, idx):
    return rdd.map(lambda fields: fields[idx]).distinct().zipWithIndex().collectAsMap()

if __name__ == '__main__':
#    if 'SPARK_HOME' not in os.environ:
#        os.environ['SPARK_HOME'] = 'F:\Spark1.5\spark-1.5.2-bin-hadoop2.6'
#    SPARK_HOME = os.environ['SPARK_HOME']
    sc = SparkContext("local[2]", "SparkRegressionModel")
    path = "hour_noheader.csv"
    
    raw_data = sc.textFile(path)
    num_data = raw_data.count()
    records = raw_data.map(lambda x: x.split(","))
#    first = records.first()
    records.cache()
#    print get_mapping(records, 2)
#    print first
#    print num_data
    mappings = [get_mapping(records, i) for i in range(2,10)]
    cat_len = sum(map(len, mappings))
    num_len = len(records.first()[11:15])
    total_len = num_len + cat_len
    print cat_len
    print num_len
    print total_len
