
# Solving questions for the book "An Introduction to Statistical Learning" by Gareth James • Daniela Witten • Trevor Hastie • Robert Tibshirani
# Zahra Rahmati
# Chapter 2

# Chapter 2 Question 7: The table below provides a training data set containing six observations, three predictors, and one qualitative response variable

import numpy as np
import pandas as pd

df = pd.DataFrame({'obs':[1, 2, 3, 4, 5, 6],
                    'X1': [0, 2, 0, 0,- 1, 1],
                  'X2': [3, 0, 1, 1, 0, 1],
                  'X3': [0, 0, 3, 2, 1, 1],
                  'Y': ["Red", "Red", "Red", "Green", "Green", "Red"]})
print(df)

# Part (a) Compute the Euclidean distance between each observation and the test point,X1 =X2 =X3 =0.
# Function euclidian_dist(x) computes the Euclidean distance for each row in a matrix x from the origin.
def euc_dist_fun(x):
    """Compute the row-wise euclidean distance from the origin"""
    return (np.sum(x**2, axis=1))**0.5

euc_dist = pd.DataFrame({'EuclideanDist': euc_dist_fun(df[['X1', 'X2','X3']])})
df_euc = pd.concat([df, euc_dist], axis=1)
print(df_euc)


# Part (b) What is our prediction with K = 1? Why?
K = 1
print(df_euc.nsmallest(K, "EuclideanDist"))

# Answer: The prediction is that Y = Green because it corresponds to the response value of the first nearest neighbor to the point point,X1 =X2 =X3 =0.

# Part (c) What is our prediction with K = 3? Why?
K= 3
print(df_euc.nsmallest(K, "EuclideanDist"))
# Answer: The prediction is that Y = Red, because 2 of the 3 nearest neighbours are Red.