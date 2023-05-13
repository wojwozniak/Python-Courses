# FCC Course: Scientific Computing with Python
# Project: Mean-Variance-Standard Deviation Calculator
# Author: Wojciech Woźniak
# Date: 13.05.2023


# Importing numpy
import numpy as np


# Main function
def calculate(list):

    # Ensuring that list contains 9 numbers
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")

    # Converting list to 3x3 matrix
    matrix = np.array(list).reshape(3, 3)

    # Calculating mean, variance, standard deviation, max, min and sum using numpy
    calculations = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix)],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)],
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)]
    }
    return calculations
