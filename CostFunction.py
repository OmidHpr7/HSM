# -*- coding: utf-8 -*-
""" **************************************************************************
                           Created on 2021

                        @author: Omid Hajipoor
                    Email: hajipoor.omid@aut.ac.ir
                  Gmail: omid.hajipoor0770@Gmail.com
************************************************************************** """

import numpy as np


def CF(x, F): #[lb,ub,dim,fobj] 

    if F=='F1':
        o=sum(pow(x,2))
            
    elif F=='F2':
        o=sum(abs(x))+np.prod(abs(x))
            
    elif F=='F3':
        Le = x.shape
        dim = Le[0]
        o=0;
        for i in range(dim+1):
            o=o+pow(sum(x[0:i]),2)
            
    elif F=='F4':
        o=max(abs(x));
            
    elif F=='F5':
        Le = x.shape
        dim = Le[0]
        o = sum((100*pow(((x[1:dim]-pow(x[0:dim-1],2))),2))+(pow((x[0:dim-1]-1),2)))
            
    elif F=='F6':
        o=sum(abs(pow((x+0.5),2)))
            
    elif F=='F7':
        Le = x.shape
        dim = Le[0]
        r=np.random.uniform(0,1,1)
        temp =  list(range(1, dim+1)) 
        o=sum((temp*pow(x,4)))+r
            
    elif F=='F8':
        o = sum(-x*(np.sin(np.sqrt(abs(x)))))
            
    elif F=='F9':
        Le = x.shape
        dim = Le[0]
        o = sum(pow(x,2)-(10*np.cos(2*np.pi*x))) + (10*dim)
            
    elif F=='F10':
        Le = x.shape
        dim = Le[0]
        o= (-20*np.exp(-0.2*np.sqrt(sum(pow(x,2))/dim)))-(np.exp(sum(np.cos(2*np.pi*x))/dim))+20+np.exp(1)
            
    elif F=='F11':
        Le = x.shape
        dim = Le[0]
        temp =  list(range(1, dim+1))
        o = (sum(pow(x,2))/4000)-np.prod(np.cos(x/np.sqrt(temp)))+1
                
    
    return o
