# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:12:06 2016

@author: liuxiangyu
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))