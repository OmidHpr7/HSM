# -*- coding: utf-8 -*-
""" **************************************************************************
                           Created on 2021
                        @author: Omid Hajipoor
                    Email: hajipoor.omid@aut.ac.ir
                  Gmail: omid.hajipoor0770@Gmail.com
************************************************************************** """

import math
import numpy as np

def lv(n,m,beta):

# This function implements Levy's flight. 
# For more information see 
# Input parameters
# n     -> Number of steps 
# m     -> Number of Dimensions 
# beta  -> Power law index  % Note: 1 < beta < 2
# Output 
# z     -> 'n' levy steps in 'm' dimension
#     num = gamma(1+beta)*sin(pi*beta/2); % used for Numerator 

    sigma_u=pow((math.gamma(1+beta)*math.sin(math.pi*beta/2)/(math.gamma((1+beta)/2)*beta*pow(2,((beta-1)/2)))),(1/beta))
    
    
#     den = gamma((1+beta)/2)*beta*2^((beta-1)/2); % used for Denominator
#     sigma_u = (num/den)^(1/beta);% Standard deviation
#     u = random('Normal',0,sigma_u^2,n,m);    
#     v = random('Normal',0,1,n,m);
    
    u = np.random.normal(0, 1, 30)*sigma_u
    v = np.random.normal(0, 1, 30)

    z = np.divide(u,(pow(abs(v), (1/beta))))
    return z
