#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 20:57:35 2023

@author: Christian
"""

import numpy as np
import cmath
import math


# Define your matrices A, B, A_inv, and B_inv
 

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

word_length = 3
all_combinations = generate_matrix_combinations([], np.identity(A.shape[0]), word_length, matrices)

print(f"Total combinations of words of length {word_length}: {all_combinations[0][2]}")

# You can print or analyze the combinations as needed
for idx, (word, result, _) in enumerate(all_combinations):
    print(f"Combination {idx + 1}:")
    for matrix in word:
        print(matrix)
    print("Resulting Matrix:")
    print(result)
    print()
