#Two state paramagnet with 100 elementary dipoles

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

N=100
Nup = np.arange(100,-1,-1)

def mult(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

multNup = []

for i in Nup:
    multNup.append(mult(100, i))

U = 100 - 2*Nup
T = (U+0.00001)/(np.log(np.asarray(multNup))+0.00001)


Tablethreetwo = pd.DataFrame([Nup, 100 - 2*Nup, -1+(2*Nup/N), multNup, np.log(np.asarray(multNup)), T , U+0.00001/T+0.00001 ])
