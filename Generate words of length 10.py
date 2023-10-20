#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 20:50:26 2023

@author: Christian
"""
import numpy as np
import random
import cmath
import math



def generate_matrix_word(A, B, word_length, random_seed=None):
    # Set a random seed if provided
    if random_seed is not None:
        random.seed(random_seed)

    # Define a list of available matrices
    matrices = [A, B, np.linalg.inv(A), np.linalg.inv(B)]

    # Initialize the result matrix with the identity matrix
    result_matrix = np.identity(A.shape[0])
    word = []

    for _ in range(word_length):
        random_matrix = random.choice(matrices)
        word.append(random_matrix)
        result_matrix = np.dot(result_matrix, random_matrix)

    return word, result_matrix

# Define your matrices A and B
A=np.array([
    [cmath.exp(-4j*math.pi/5),0,0],
    [0,cmath.exp(3j*math.pi/5),0],
    [0, 0, cmath.exp(3j*math.pi/5)]
    ]) 


tau=(math.sqrt(5)-1)/2


B= np.array([
    [-1*tau* cmath.exp(-1j*math.pi/5), math.sqrt(tau)*cmath.exp(-3j*math.pi/5),0],
    [math.sqrt(tau)*cmath.exp(-3j*math.pi/5), -1*tau, 0],
    [0,0,cmath.exp(3j*math.pi/5)]
    ])

 

# Set a random seed for reproducibility (optional)
random_seed = 2

# Generate a word of matrices and get the resulting matrix
word, result = generate_matrix_word(A, B, 10, random_seed)

print("Generated Word of Matrices:")
for matrix in word:
    print(matrix)
print("Resulting Matrix after Multiplication:")
print(result)
