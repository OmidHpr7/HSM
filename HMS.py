# -*- coding: utf-8 -*-
""" **************************************************************************
                           Created on 2021

                        @author: Omid Hajipoor
                    Email: hajipoor.omid@aut.ac.ir
                  Gmail: omid.hajipoor0770@Gmail.com
************************************************************************** """

#Human Mental search 

from CostFunction import CF
from Functions_details import initialization
import numpy as np
import random
from levy import lv
from sklearn.cluster import KMeans




def HMS(nPop, MaxIt, VarMin, VarMax, NVar, F):
    #NVar=Params.nFeaturs;% Number of Variables
    NPop=nPop       #Number of bids
    K=5            #Number of cluster
    C=2
    MaxIter=MaxIt  #Maximum Iteration
    ML=2           #Minimum mental process
    MH=10          #Maximum mental precess
    L=0.3          #lower bound
    U=1.99         #Upper bound
    
    
    
    
    #Initialization

    X = initialization(NVar,NPop,VarMin,VarMax); # initialize a population of Npop bids
    X_Star = np.zeros((1,NVar))
    Iter = 0;  # current iteration number
    Cost_Bid =np.zeros((NPop,1))  # store fitness value for each Bid
    Best_Iter=np.zeros((MaxIter,1)) #Best fittness for each Iteration
    X_plus=np.zeros((1,NVar)) #best bid in the current Bids
    Cost_X_Star=np.inf  #the best cost of bids in the initial population
    Cost_X_plus=np.inf  #the best cost of bids in the current population
    
    for i in range(NPop):
        Cost_Bid[i,0] = CF(X[i,:], F) #Calculate the Cost of bids
        if  Cost_Bid[i,0] < Cost_X_Star:
             Cost_X_Star= Cost_Bid[i,0]
             X_Star=X[i,:]  #find the best bid in the initial population
     
        
    X_Star = X_Star.reshape(1,NVar) 
    NS=np.zeros((MH, NVar))
    
    # Now start the Iteration
    while Iter < MaxIter:
        # Mental Search
        
        for i in range(NPop):
            q=random.randint(ML,MH) #Produce new solutions with help mental search
            beta=np.random.uniform(L,U) #Power law index  % Note: 0 < beta < 2
            MenSearch_Cost = []
            for i in range(q):
                MenSearch_Cost.append(np.inf)
            for k in range(q):
                t1 = (2-Iter*(2/MaxIter))
                t2 = lv(1,NVar,beta)
                t3 = X[i,:]-X_Star[0,:]
                S=t1*np.multiply(0.01, np.multiply(t2, t3));
                S = S.reshape(1,NVar)
                NS[k,:]=X[i,:]+S;

                MenSearch_Cost[k] = CF(NS[k,:], F)
                if MenSearch_Cost[k]< Cost_Bid[i]:
                  Cost_Bid[i]=  MenSearch_Cost[k]
                  X[i,:]=NS[k,:]
        
        ### Clustering Current Population
        kmeans = KMeans( init="random", n_clusters=K, n_init=10, max_iter=100, verbose=0)
        cluster = kmeans.fit(X, K).labels_ 
        
        #MeanCost_Cluster= 100000*ones(C,1); 
        Winner_Cluster_cost=np.inf
        number_in_cluster = np.zeros((K,1))
        
        # Determine the number of members of each cluster
        for i in range(NPop):
            number_in_cluster[cluster[i]]= number_in_cluster[cluster[i]] + 1
        
        
        # Initialization cluster
        Cost_Cluster = {}
        Index_Cluster = {}
        for k in range(K):
            counter = 0
            Cost_Cluster[k] = []
            Index_Cluster[k] = []
            for i in range(NPop):
                if cluster[i]==k:
                    counter=counter+1;
                    Cost_Cluster[k].append(Cost_Bid[i][0])  
                    Index_Cluster[k].append(i)
            
        
        
        ## Evalute Clusters and calculate the average cost of each cluster and find the winning cluster
        MeanCost_Cluster = np.zeros((K,1))
        
        for k in range(K):
            MeanCost_Cluster[k] = np.mean(Cost_Cluster[k])
            if  MeanCost_Cluster[k]< Winner_Cluster_cost:
                Winner_Cluster_cost = MeanCost_Cluster[k]
                Winner_Cluster=k;
        
        # ind the winning bid
        point=np.argmin(Cost_Cluster[Winner_Cluster])
        ind = Index_Cluster[Winner_Cluster]
        Winner_index= ind[point]
        Winner_bid=X[Winner_index,:]
        
        
        '''  *************************************************************************************** '''
        # Moving bids toward the best strategy
        for i in range(NPop):
            for n in range(NVar):
                r=np.random.uniform(0,1,1);
                X[i,n]=X[i,n]+C*(r* Winner_bid[n]-X[i,n])
                
            Cost_Bid[i] = CF(X[i,:], F);
            if Cost_X_plus > Cost_Bid[i,0]: #% Find best bid in the current population
                Cost_X_plus = Cost_Bid[i,0];
                X_plus=X[i,:]
                
        X_plus = X_plus.reshape(1,NVar) 
        if Cost_X_Star > Cost_X_plus:
            Cost_X_Star=Cost_X_plus
            X_Star =X_plus
            
        Best_Iter[Iter]=Cost_X_Star
        Iter=Iter+1
        print(Cost_X_Star)
        
    ret = CF(X_Star, F)
    if type(ret) == np.ndarray:
        return sum(ret)
    else:
        return ret

            
