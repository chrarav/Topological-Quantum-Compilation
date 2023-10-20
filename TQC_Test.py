#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:19:32 2023

@author: Christian
"""


import numpy as np
import cmath
import math


# Define your matrices A=sigma1, B=sigma2, A_inv, and B_inv
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

 
A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)

matrices = [A, B, A_inv, B_inv]

def generate_matrix_combinations(current_word, current_result, word_length, matrices, count=0):
    if word_length == 0:
        return [(current_word, current_result, count + 1)]
    combinations = []
    for matrix in matrices:
        new_word = current_word + [matrix]
        new_result = np.dot(current_result, matrix)
        combinations += generate_matrix_combinations(new_word, new_result, word_length - 1, matrices, count)
    return combinations


def find_closest_matrix(combinations, target_matrix):
    closest_matrix = None
    min_error = float('inf')
    for word, result, _ in combinations:
        if result.shape == target_matrix.shape:
            spectral_norm_diff = np.linalg.norm(result, 2) - np.linalg.norm(target_matrix, 2)
            if abs(spectral_norm_diff) < min_error:
                min_error = abs(spectral_norm_diff)
                closest_matrix = result
    return closest_matrix, min_error

word_length = 4
cnot = np.array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]])



"Calculate SU(2) matrix of cnot for the real variable =1"
cnot_SU2=cmath.exp(-1j*math.pi/4)*cnot

Q=1/math.sqrt(2)*np.array([
    [1, 0, 0, 1], 
    [0, 1j, 1j, 0],
    [0, 1, -1, 0],
    [1j, 0, 0, -1j]
    ])


conjugate_Q=np.conjugate(Q)

cnot_SU2_B = np.dot(conjugate_Q, np.dot(cnot_SU2, Q))
cnot_SU2_B_transpose=np.transpose(cnot_SU2_B)
m=np.dot(cnot_SU2_B_transpose, cnot_SU2_B)

target_matrix = m  
all_combinations = generate_matrix_combinations(np.identity(3), np.identity(3), word_length, matrices)
closest_matrix, error = find_closest_matrix(all_combinations, target_matrix)

print(f"Total combinations of words of length {word_length}: {all_combinations[0][2]}")

if closest_matrix is not None:
    print(f"Closest Matrix to the Target Matrix:")
    print(closest_matrix)
    print(f"Error (Operator Norm): {error}")
else:
    print("No combinations matched the target matrix.")