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
        o=max(abs(x))
            
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
        
    elif F=='F12':
        Le = x.shape
        dim = Le[0]
        o=((np.pi/dim)*((10*(pow((np.sin(np.pi*(1+((x[0]+1)/4)))), 2)))+(sum((pow(((x[0:dim-1]+1)/4),2))*(1+(10*pow((np.sin(np.pi*(1+((x[1:dim]+1)/4)))),2)))))+(pow(((x[dim-1]+1)/4),2))))+(sum(Ufun(x,10,100,4)))

        
    elif F=='F13':
        Le = x.shape
        dim = Le[0]
        o = (0.1 * ( (pow(np.sin(3*np.pi*x[0]) , 2)) + (sum( (pow((x[0:dim-1]-1), 2)) * (pow( (1+(np.sin(3*np.pi*x[1:dim]))) , 2)) )) + ( (pow((x[dim-1]-1),2)) * (1+pow( np.sin(2*np.pi*x[dim-1]) , 2)) ))) + (sum(Ufun(x,5,100,4)))
        
        
    elif F=='F14':
        aS=[[-32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32],
            [-32, -32, -32, -32, -32, -16, -16, -16, -16, -16, 0, 0, 0, 0, 0, 16, 16, 16, 16, 16, 32, 32, 32, 32, 32]]
        aS = np.array(aS)
        bS = []
        
        x = x.reshape((len(x),))
        for i in range(25):
            bS.append(sum(pow((x.T-aS[:,i]),6)))

        temp = list(range(1, 26))
        temp = np.array(temp)

        o=pow(((1/500)+sum(1/(temp+bS))),(-1));
            
          
    elif F=='F15':
        aK=[.1957, .1947, .1735, .16, .0844, .0627, .0456, .0342, .0323, .0235, .0246];
        bK=[.25, .5, 1, 2, 4, 6, 8, 10, 12, 14, 16]
        
        aK = np.array(aK)
        bK = np.array(bK)
        
        bK=1/bK
        o=sum(pow((aK-((x[0]*(pow(bK,2)+(x[1]*bK)))/(pow(bK,2)+(x[2]*bK)+x[3]))),2))
        
        
    elif F=='F16':
        o=4*(pow(x[0],2))-2.1*pow(x[0],4)+pow(x[0],6)/3+x[0]*x[1]-4*pow(x[1],2)+4*pow(x[1],4)
            
          
    elif F=='F17':
        o=pow((x[1]-pow(x[0],2)*5.1/(4*pow(np.pi,2))+5/np.pi*x[0]-6),2)+10*(1-1/(8*np.pi))*np.cos(x[0])+10
             
             
    elif F=='F18':
        o=(1+pow((x[0]+x[1]+1),2)*(19-14*x[0]+3*pow(x[0],2)-14*x[1]+6*x[0]*x[1]+3*pow(x[1],2)))*(30+pow(2*x[0]-3*x[1],2)*(18-32*x[0]+12*pow(x[0],2)+48*x[1]-36*x[0]*x[1]+27*pow(x[1],2)))
            
          
    elif F=='F19':
        aH=np.array([[3, 10, 30],[.1, 10, 35], [3, 10, 30], [.1, 10, 35]])
        cH=np.array([1, 1.2, 3, 3.2])
        pH=np.array([[.3689, .117, .2673], [.4699, .4387, .747], [.1091, .8732, .5547], [.03815, .5743, .8828]])
        o=0
        for i in range(4):
            o=o-cH[i]*np.exp(-(sum(aH[i,:]*pow((x-pH[i,:]),2))))
            
            
    elif F=='F20':
        aH=np.array([[10, 3, 17, 3.5, 1.7, 8],[.05, 10, 17, .1, 8, 14], [3, 3.5, 1.7, 10, 17, 8], [17, 8, .05, 10, .1, 14]])
        cH=np.array([1, 1.2, 3, 3.2])
        pH=np.array([[.1312, .1696, .5569, .0124, .8283, .5886], [.2329, .4135, .8307, .3736, .1004, .9991], 
                     [.2348, .1415, .3522, .2883, .3047, .6650], [.4047, .8828, .8732, .5743, .1091, .0381]])
        o=0; 
        for i in range(4):
            o=o-cH[i]*np.exp(-(sum(aH[i,:]*pow((x-pH[i,:]),2))))
            
            
    elif F=='F21':
        aSH=np.array([[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], 
                      [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1], [6, 2, 6, 2], [7, 3.6, 7, 3.6]])
        cSH=np.array([.1, .2, .2, .4, .4, .6, .3, .7, .5, .5])
        o=0;
        for i in range(5):
            o=o-pow((np.dot((x-aSH[i,:]),(x-aSH[i,:]))+cSH[i]),(-1))
            
            
    elif F=='F22':
        aSH=np.array([[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1], [6, 2, 6, 2], [7, 3.6, 7, 3.6]])
        cSH=np.array([.1, .2, .2, .4, .4, .6, .3, .7, .5, .5])
        o=0;
        for i in range(7):
            o=o-pow((np.dot((x-aSH[i,:]),(x-aSH[i,:]))+cSH[i]),(-1))
            
            
    elif F=='F23':
        aSH=np.array([[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1], [6, 2, 6, 2], [7, 3.6, 7, 3.6]])
        cSH=np.array([.1, .2, .2, .4, .4, .6, .3, .7, .5, .5])
        o=0;
        for i in range(10):
            o=o-pow((np.dot((x-aSH[i,:]),(x-aSH[i,:]))+cSH[i]),(-1))
                
    
    return o
