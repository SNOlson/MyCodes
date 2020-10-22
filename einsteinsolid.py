"""Table for 200 and 100 oscillators with 100 units of energy"""
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def mult(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

nA = 200
nB = 100
qA = np.arange(0,101,1)
qB = np.arange(101, 0, -1)

#multsA = [mult(n = i+nA-1, r = i) for i in qA]
#multsB = [mult(n = j+nB-1, r = i) for j in qB]

multA = []
multB = []

for i in qA:
    multA.append(mult(n = i+nA-1, r = i))

for i in qB:
    multB.append(mult(n = i + nB - 1, r=i))

multsA = np.asarray(multA)
multsB = np.asarray(multB)



#multsA = np.asarray(list(map(mult(n = qA+nA-1,r = qA))))
#multsB = np.asarray(list(map(mult(n = qB+nB-1,r = qB))))

Einstein = pd.DataFrame(data = [qA, multsA, qB, multsB, multsA*multsB])

#plt.plot(numHeads, probs)
#plt.title("Probabilites of getting n heads flipping 50 coins")
#plt.xlabel("n Heads")
#plt.ylabel("Probability")
#plt.show()
plt.plot(qA, Einstein.T[4])
