import numpy as np  ## for matrices 
import pandas as pd ## for importing xlxs  

## loading the required sheet 
file_path = "/Users/niteshnirranjan/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='Purchase data')

## Segregating into two different matrices 
A = df.iloc[0:11,1:4].values
C = df.iloc[:,4].values

## Dimension of the matrices
dimension_A = A.shape
dimension_C = C.shape

## Rank of Matrix A 
rank_A = np.linalg.matrix_rank(A)

## Pseudo inverse of Matrix A 
pseudo_A = np.linalg.pinv(A)

X = pseudo_A.dot(C)

print("Matrix A :",A)
print("Matrix C :",C)

print("Dimension of A:",dimension_A)
print("Dimension of C:",dimension_C)

print("Rank of A :",rank_A)
print("Prices of each product :",X)