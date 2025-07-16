import numpy as np  ## for matrices 
import pandas as pd ## for importing xlxs  
import statistics ## for mean and median 

## loading the required sheet 
file_path = "/Users/niteshnirranjan/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='IRCTC Stock Price')

## splitting the required matrix
X = df.iloc[:,3]

## Finding mean and median 
mean_X = statistics.mean(X)
median_X = statistics.median(X)

print("Mean Price :",mean_X)
print("Median Price :",median_X)