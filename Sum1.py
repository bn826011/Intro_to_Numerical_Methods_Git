# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:07:58 2017

@author: bn826011
"""

import numpy as np

def sumatoN(a, N):
    "Sum number a N times"
    
    #This will not work with large N for reasons discussed yesterday
    
    Sum = 0
    
    for counter in xrange(N):
        
        Sum += a
        
    return Sum
        
        
def sumatoNbetter(a, N):
    "Sum number a N times"
    "Hopefully avoid running out of space in the mantissa"
    
    #The idea is to put a as a length N array, then split that array into
    #chunks of size small enough that they can be summed without incurring 
    #excessive error
        