# -*- coding: utf-8 -*-
"""
Define matrices A:=sigma1, B:=sigma2, CNOT 
and the associated  matrix m from CNOT
as NumPy arrays
"""

import numpy as np
import cmath
import math
from itertools import product

# Define matrices A:=sigma1, B:=sigma2, CNOT 
# and the associated  matrix m from CNOT
# as NumPy arrays

A=np.array([
    [cmath.exp(-4j*math.pi/5),0,0],
    [0,cmath.exp(3j*math.pi/5),0],
    [0, 0, cmath.exp(3j*math.pi/5)]
    ]) 


tau=(math.sqrt(5)-1)/2

B = np.array([
    [-1*tau* cmath.exp(-1j*math.pi/5), math.sqrt(tau)*cmath.exp(-3j*math.pi/5),0],
    [math.sqrt(tau)*cmath.exp(-3j*math.pi/5), -1*tau, 0],
    [0,0,cmath.exp(3j*math.pi/5)]
    ])

 

# Define your matrices A and B as NumPy arrays

"Calculate SU(2) matrix of cnot for the real variable φ=1"


cnot = np.array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]])


cnot_SU2=cmath.exp(-1j*math.pi/4)*cnot

Q=1/math.sqrt(2)*np.array([
    [1,0,0,1], 
    [0, 1j, 1j, 0],
    [0,1,-1,0],
    [1j, 0, 0, -1j]
    ]
    )


conjugate_Q=np.conjugate(Q)

cnot_SU2_B = np.dot(conjugate_Q, np.dot(cnot_SU2, Q))
cnot_SU2_B_transpose=np.transpose(cnot_SU2_B)
m=np.dot(cnot_SU2_B_transpose, cnot_SU2_B)
print(m) 
