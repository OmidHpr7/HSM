# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 19:49:09 2021

@author: acer
"""

import math
import numpy as np

def lv(n,m,beta):

    sigma_u=pow((math.gamma(1+beta)*math.sin(math.pi*beta/2)/(math.gamma((1+beta)/2)*beta*pow(2,((beta-1)/2)))),(1/beta));
    
    u = np.random.normal(0, 1, 30)*sigma_u
    v = np.random.normal(0, 1, 30)

    z = np.divide(u,(pow(abs(v), (1/beta))))
    return z