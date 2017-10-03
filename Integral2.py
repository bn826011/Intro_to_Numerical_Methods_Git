# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:20:45 2017

@author: bn826011

File contains function to integrate arbitrary function between specified
endpoints, and specific functions to use as an input
"""

from __future__ import division
import numpy as np

def integratef(f,a, b, gridpoints):
    "Numerically integrates function f"
    "Between limits a and b"
    "With gridpoints gridpoints"
    "Using one point Gaussian quadrature"
    
    if not(isinstance(gridpoints, int)):
        raise TypeError('Argument gridpoints must be an integer')
    
    Sum = 0
    
    intervalwidth = (b-a)/gridpoints
    
    # Number of gridpoints to get resolution res
    
    if intervalwidth != 0:
        break
    else:
        raise Exception("The interval width is zero, so numerical integration will fail")
    
    
    
    for counter in xrange(gridpoints):
        
        midpoint = a + (counter+1/2)*intervalwidth
        
        Sum += f(midpoint)
        
    # Loops over gridpoints and sums contributions to integral
    
    Sum /= gridpoints
    
    # Scales according to width
    
    return Sum
    
    
    
def f(x):
    "Function of a single variable"
    "Unhelpfully named"
    
    return 3*x - 2
    

def sinm(x):
    "Sin of m*x"
    
    return np.sin(x)
