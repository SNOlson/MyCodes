"""Probability Plot for 50 coins"""
import math
import matplotlib.pyplot as plt
import numpy as np

def prob(r, n = 50, p = 2):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r)) / 2**n

numHeads = np.arange(0,51,1)
probs = list(map(prob, numHeads))

plt.plot(numHeads, probs)
plt.title("Probabilites of getting n heads flipping 50 coins")
plt.xlabel("n Heads")
plt.ylabel("Probability")
plt.show()
