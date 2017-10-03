'''Script to perform obligatory error checking'''

import numpy as np

from Integral2 import integratef

assert abs(integratef(np.sin, 0, 2*np.pi, 100)) < 1e-6, \
       "integratef returned a non zero result for the integral of \
       sin between 0 and 2 pi"
       
# Should make sure that my function can integrate sin

try:
    integratef(7, 0, 1, 100)
except:
    pass
else:
    print("An exception really should be raised, as 7 is not callable")

    
try:
    integratef(np.sin, 1, 1, 100)
except:
    pass
else:
    print("An exception should be raised, as the interval width is zero")
