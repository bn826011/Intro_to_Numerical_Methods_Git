# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:20:45 2017

@author: bn826011
"""
from __future__ import division
import numpy as np

def integratef(f,a, b, gridpoints):
    "Numerically integrates function f"
    "Between limits a and b"
    "With gridpoints gridpoints"
    "Using one point Gaussian quadrature"
    
    Sum = 0
    
    intervalwidth = (b-a)/gridpoints
    
    # Number of gridpoints to get resolution res
    
    for counter in xrange(gridpoints):
        
        midpoint = a + (counter+1/2)*intervalwidth
        
        Sum += f(midpoint)
        
    
    Sum /= gridpoints
    
    return Sum
    
    
    
def f(x):
    "Function of a single variable"
    "Unhelpfully named"
    
    return 3*x - 2
    

def sinm(x):
    "Sin of m*x"
    
    return np.sin(x)