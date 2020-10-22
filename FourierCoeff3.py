# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:42:08 2018

@author: Syd Olson
"""
import numpy as np
import matplotlib.pyplot as plt

#Variables
t0 = -1
tf = 1
m_array = np.linspace(-1,1,1)
t_array = np.linspace(-1,1,1000)
G_array = np.zeros_like(t_array)*np.exp(0j)
true_G = 3*np.sin(t_array*np.pi/3)

A1 = (1/((np.pi/3)-np.pi*m_array))*np.sin(((np.pi/3)-np.pi*m_array)*tf)
A2 = (1/((np.pi/3)-np.pi*m_array))*np.sin(((np.pi/3)-np.pi*m_array)*t0)
B1 = (1/((np.pi/3)+np.pi*m_array))*np.sin(((np.pi/3)+np.pi*m_array)*tf)
B2 = (1/((np.pi/3)+np.pi*m_array))*np.sin(((np.pi/3)+np.pi*m_array)*t0)
cm = (-3j/4)*((A1-A2)-(B1-B2))
print (cm)

for m in range (len(m_array)):
    G = cm[m]*np.exp(1j*2*m_array[m]*t_array*np.pi/(tf-t0))
    G_array += G
    
print (G)

plt.plot(t_array, G_array,label='Fourier')
plt.plot(t_array,true_G,label='Correct')
plt.title("Fourier Series")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("t")
plt.ylabel("y")
plt.axis("tight")
plt.legend()
plt.show()

m_array = np.linspace(-3,3,6)
t_array = np.linspace(-1,1,1000)
G_array = np.zeros_like(t_array)*np.exp(0j)
true_G = 3*np.sin(t_array*np.pi/3)

A1 = (1/((np.pi/3)-np.pi*m_array))*np.sin(((np.pi/3)-np.pi*m_array)*tf)
A2 = (1/((np.pi/3)-np.pi*m_array))*np.sin(((np.pi/3)-np.pi*m_array)*t0)
B1 = (1/((np.pi/3)+np.pi*m_array))*np.sin(((np.pi/3)+np.pi*m_array)*tf)
B2 = (1/((np.pi/3)+np.pi*m_array))*np.sin(((np.pi/3)+np.pi*m_array)*t0)
cm = (-3j/4)*((A1-A2)-(B1-B2))
print (cm)

for m in range (len(m_array)):
    G = cm[m]*np.exp(1j*2*m_array[m]*t_array*np.pi/(tf-t0))
    G_array += G
    
print (G)

plt.plot(t_array, G_array,label='Fourier')
plt.plot(t_array,true_G,label='Correct')
plt.title("Fourier Series")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("t")
plt.ylabel("y")
plt.axis("tight")
plt.legend()
plt.show()

m_array = np.linspace(-5,5,11)
t_array = np.linspace(-1,1,1000)
G_array = np.zeros_like(t_array)*np.exp(0j)
true_G = 3*np.sin(t_array*np.pi/3)

A1 = (1/((np.pi/3)-np.pi*m_array))*np.sin(((np.pi/3)-np.pi*m_array)*tf)
A2 = (1/((np.pi/3)-np.pi*m_array))*np.sin(((np.pi/3)-np.pi*m_array)*t0)
B1 = (1/((np.pi/3)+np.pi*m_array))*np.sin(((np.pi/3)+np.pi*m_array)*tf)
B2 = (1/((np.pi/3)+np.pi*m_array))*np.sin(((np.pi/3)+np.pi*m_array)*t0)
cm = (-3j/4)*((A1-A2)-(B1-B2))
print (cm)

for m in range (len(m_array)):
    G = cm[m]*np.exp(1j*2*m_array[m]*t_array*np.pi/(tf-t0))
    G_array += G
    
print (G)

plt.plot(t_array, G_array,label='Fourier')
plt.plot(t_array,true_G,label='Correct')
plt.title("Fourier Series")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("t")
plt.ylabel("y")
plt.axis("tight")
plt.legend()
plt.show()

m_array = np.linspace(-25,25,51)
t_array = np.linspace(-1,1,1000)
G_array = np.zeros_like(t_array)*np.exp(0j)
true_G = 3*np.sin(t_array*np.pi/3)

A1 = (1/((np.pi/3)-np.pi*m_array))*np.sin(((np.pi/3)-np.pi*m_array)*tf)
A2 = (1/((np.pi/3)-np.pi*m_array))*np.sin(((np.pi/3)-np.pi*m_array)*t0)
B1 = (1/((np.pi/3)+np.pi*m_array))*np.sin(((np.pi/3)+np.pi*m_array)*tf)
B2 = (1/((np.pi/3)+np.pi*m_array))*np.sin(((np.pi/3)+np.pi*m_array)*t0)
cm = (-3j/4)*((A1-A2)-(B1-B2))
print (cm)

for m in range (len(m_array)):
    G = cm[m]*np.exp(1j*2*m_array[m]*t_array*np.pi/(tf-t0))
    G_array += G
    
print (G)

plt.plot(t_array, G_array,label='Fourier')
plt.plot(t_array,true_G,label='Correct')
plt.title("Fourier Series")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("t")
plt.ylabel("y")
plt.axis("tight")
plt.legend()
plt.show()
