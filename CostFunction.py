# -*- coding: utf-8 -*-
""" **************************************************************************
                           Created on 2021

                        @author: Omid Hajipoor
                    Email: hajipoor.omid@aut.ac.ir
                  Gmail: omid.hajipoor0770@Gmail.com
************************************************************************** """

import numpy as np


def CF(x, F): 

    if F=='F1':
        o=sum(pow(x,2))
            
    elif F=='F2':
        o=sum(abs(x))+np.prod(abs(x))
            
    elif F=='F3':
        o=0;
        for i in range(len(x)):
            sm = sum(x[0:i])
            o=o+pow(sm,2)
            
    elif F=='F4':
        o=max(abs(x))
            
    #elif F=='F5':
     #   dim=len(x)
     #   o=sum(100*(x[1:dim]-pow(pow(x[0:dim-1],2),2))+pow((x[0:dim-1]-1),2))
            
    elif F=='F6':
        o=sum(pow(abs((x+.5)),2))
        
        
    '''elif F=='F7':
            lb=-1.28;
            ub=1.28;
            dim=30;
            
    elif F=='F8':
            lb=-500;
            ub=500;
            dim=30;
            
    elif F=='F9':
            lb=-5.12;
            ub=5.12;
            dim=30;
            
    elif F=='F10':
            lb=-32;
            ub=32;
            dim=30;
            
    elif F=='F11':
            lb=-600;
            ub=600;
            dim=30;
            
    elif F=='F12':
            lb=-50;
            ub=50;
            dim=30;
            
    elif F=='F13':
            lb=-50;
            ub=50;
            dim=30;
            
    elif F=='F14':
            lb=-65.536;
            ub=65.536;
            dim=2;
            
    elif F=='F15':
            lb=-5;
            ub=5;
            dim=4;
            
    elif F=='F16':
            lb=-5;
            ub=5;
            dim=2;
            
    elif F=='F17':
            lb=[-5,0];
            ub=[10,15];
            dim=2;
            
    elif F=='F18':
            lb=-2;
            ub=2;
            dim=2;
            
    elif F=='F19':
            lb=0;
            ub=1;
            dim=3;
            
    elif F=='F20':
            lb=0;
            ub=1;
            dim=6;     
            
    elif F=='F21':
            lb=0;
            ub=10;
            dim=4;    
            
    elif F=='F22':
            lb=0;
            ub=10;
            dim=4;    
            
    elif F=='F23':
            lb=0;
            ub=10;
            dim=4;     '''       
    
    return o
