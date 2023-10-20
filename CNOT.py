#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:49:52 2023

@author: Christian
"""

import cmath 
from math  import sqrt, pi
from numpy import array, conjugate, dot, transpose
import sympy as sym

#CNOT gate
cnot = array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]])
print(cnot)

print()


#Generic variable x
x = sym.Symbol('x')

#The SU(2)-matrix obtained from CNOT
#Exp called from sympy to capture the generic variable x
cnot_SU2=sym.exp(-1j*x*pi/4)*cnot 
print(cnot_SU2)

print()


#Matrix @
Q=1/sqrt(2)*array([
    [1,0,0,1], 
    [0, 1j, 1j, 0],
    [0,1,-1,0],
    [1j, 0, 0, -1j]
    ])
print(Q)

print()

#Complex conjugate Q
conjugate_Q=conjugate(Q)
print(conjugate_Q)

print()

#Matrix (CNOT_SU2)_B
cnot_SU2_B = dot(conjugate_Q, dot(cnot_SU2, Q))
print(cnot_SU2_B)


print()

#The transpose of CNOT_SU2_B
cnot_SU2_B_transpose=transpose(cnot_SU2_B)
print(cnot_SU2_B_transpose)

print()

#Matrix of interest m
m=dot(cnot_SU2_B_transpose, cnot_SU2_B)
print(m) 
