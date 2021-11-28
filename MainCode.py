# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 14:26:00 2021

@author: acer
"""

from Functions_details import Functions_details
from HMS import HMS

Function_name='F6';
VarMin,VarMax,nVar,CostFunction=Functions_details(Function_name);


#Set General Params
MaxIt =500;
nPop  =30 ;



MaxRun=2;

results = []
for r in range(MaxRun):
    print('====================================================')
    print(' Start of  \n',r)
    print('====================================================')
    
    Out_HMS = HMS(nPop, MaxIt,VarMin,VarMax,nVar,CostFunction)
    results.append((Out_HMS))