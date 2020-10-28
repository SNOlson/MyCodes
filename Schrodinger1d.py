# coding: utf-8
#Distributed under the terms of the Apache 2.0 License.

__author__ = "Sydney Olson"
__copyright__ = "Copyright 2020, Sydney Olson"
__maintainer__ = "Sydney Olson"
__email__ = "snolson1@asu.edu"
__date__ = "October 27, 2020"



"""Solving the 1D Schrodinger Equation for a QHO by Variational Method
--------------------------------------------------------------------------------
Steps:
1) Pick a potential function
2) Pick a trial wavefunction
3) Calculate the expectation value of the hamiltonian divided by the inner
product of separate level wavefunctions
--------------------------------------------------------------------------------
Atomic Units:
Reduced Planck constant:  hbar = 1, also known as the atomic unit of action
Elementary charge: e=1, also known as the atomic unit of charge
Bohr radius: a_0 = 1, also known as the atomic unit of length
Electron mass: m_e=1, also known as the atomic unit of mass
--------------------------------------------------------------------------------
time hbar/E_h	2.4188843265857(47)×10−17 s


vibrational frequency of HCl -> 8.88*10**13 Hz
-> 3.67*10^31 atomic unit Hertz
https://phys.libretexts.org/Bookshelves/University_Physics/
Book%3A_University_Physics_(OpenStax)/
Map%3A_University_Physics_III_-_Optics_and_Modern_Physics_(OpenStax)/
07%3A_Quantum_Mechanics/7.06%3A_The_Quantum_Harmonic_Oscillator

Example 7.6.2"""

import math
import numpy as np
import scipy as scp

"""Steps:
1) Pick a potential function
2) Pick a trial wavefunction
3) Calculate the expectation value of the hamiltonian divided by the inner
product of separate level wavefunctions
    3a) Finite differences second order derivative of trial wavefunction as per
    definition of <T>
    3b) Integrate result of <T>, <V> and <psi*|psi> over boundaries
    3c) Divide <T>+<V> by <psi*|psi>
    3d) Differentiate with respect to scaling parameter and minimize energy"""





numrange = np.linspace(-2*np.pi, 2*np.pi, 1000)

def gaussianwavefun(x):
    return (2/np.pi)**4*np.exp(-x**2)

def potential(x):
    return 1/2*x**2

def identity(x):
    return x

def secondOrderCentralDifference(f, x, h):
    numdiff = f(x+h)-2*f(x)+f(x-h)
    return numdiff

#def trapezoidalIntegration(fa, fb , boundaries):
#    numint = (boundaries[0]-boundaries[-1])*(fa+fb) / 2
#    return numint

def MCQuantumProd1D(fs, boundaries, steps):
    intrange = np.linspace(boundaries[0], boundaries[-1], steps)
    numfuncs = [fs[0](intrange), fs[1](intrange), fs[0](intrange)]
    product = numfuncs[0]*numfuncs[1]*numfuncs[2]
    rpicks = [product[step] for step in np.random.randint(0, steps, int(1/2*steps))]
    mcintegral = (boundaries[-1]-boundaries[0])/len(rpicks)*np.sum(rpicks)
    return mcintegral

MCexpectationV = MCQuantumProd1D([gaussianwavefun, potential], [-2*np.pi,2*np.pi], 1000)

#MCexpectationT = MCQuantumProd1D([])

MCmodsquared = MCQuantumProd1D([gaussianwavefun, identity],  [-2*np.pi,2*np.pi], 1000)

#wavefunction = gaussianwavefun(numrange)

#h=0.001

#secDiff = gaussianwavefun(numrange-h) - 2*gaussianwavefun(numrange)\
# + gaussianwavefun(numrange+h)

#expectationT = -1/2*((numrange[-1] - numrange[0])*(((wavefunction*secDiff)[0]\
#+(wavefunction*secDiff)[-1])/2))

#innerprod = (numrange[-1] - numrange[0])*(((gaussianwavefun(numrange)**2)[0]+(gaussianwavefun(numrange)**2)[-1])/2)

#expectationV = (numrange[-1] - numrange[0])*(((wavefunction*potential(numrange, omega=1)\
#*wavefunction[0])+(wavefunction*potential(numrange, omega=1)\
#*wavefunction)[-1])/2)

#expectationH = expectationT + expectationV

#expoverinner = expectationH / innerprod

#expH = -1/2*trapezoidalIntegration(fa = gaussianwavefun(x=numrange[0])*\
#secondOrderCentralDifference(gaussianwavefun(x=numrange[0]),
#h=0.01, boundaries=numrange[0]),fb = gaussianwavefun(x=numrange[-1])*\
#secondOrderCentralDifference(gaussianwavefun(x=numrange[-1]),
#h=0.01, boundaries=numrange[-1]), boundaries=numrange)

#expV = trapezoidalIntegration(fa = gaussianwavefun(x=numrange[0])*\
#potential(x=numrange[0], omega = 2.307E31)*gaussianwavefun(x=numrange[0]),
#fb = gaussianwavefun(x=numrange[-1])*potential(x=numrange[-1],
#omega = 2.307E31)*gaussianwavefun(x=numrange[-1]), boundaries=numrange)

#innerprod = trapezoidalIntegration(fa = gaussianwavefun(x=numrange[0])*\
#gaussianwavefun(x=numrange[0]),fb=gaussianwavefun(x=numrange[-1])*\
#gaussianwavefun(x=numrange[-1]),boundaries=numrange)

#varE = (expH + expV) / innerprod
#print(varE)
