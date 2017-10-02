'''Script to perform obligatory error checking'''

import numpy as np

assert abs(integratef(np.sin, 0, 2*np.pi, 100)) < 1e-6, \
       "integratef returned a non zero result for the integral of sin between 0 and 2 pi"
       
# Should make sure that my function can integrate sin

try:
    integratef(np.sin, 0, 2*np.pi, 100)
except TypeError:
    print("One of the input variables is of the wrong type")
    # gridpoint
    pass
    # is that necesary?
    
try:
    integratef(np.sin, 0, 2*np.pi, 100)
except:
    pass
