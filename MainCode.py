# -*- coding: utf-8 -*-
""" **************************************************************************
                           Created on 2021
                        @author: Omid Hajipoor
                    Email: hajipoor.omid@aut.ac.ir
                  Gmail: omid.hajipoor0770@Gmail.com
************************************************************************** """


from Functions_details import Functions_details
from HMS import HMS

Function_name = 'F1';
VarMin,VarMax,nVar,CostFunction = Functions_details(Function_name);


#Set General Params
MaxIt  = 500;
nPop   = 30 ;
MaxRun = 2;


results = []
for r in range(MaxRun):
    print('====================================================')
    print(' Start of  \n',r)
    print('====================================================')
    
    # Run Optimization Algorithms BGWO1
    Out_HMS = HMS(nPop, MaxIt,VarMin,VarMax,nVar,CostFunction)
    results.append((Out_HMS))
