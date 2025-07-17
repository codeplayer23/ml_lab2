import numpy as np  ## for matrices 
import pandas as pd ## for importing xlxs  
import statistics ## for mean and median 

## loading the required sheet 
file_path = "/Users/niteshnirranjan/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='IRCTC Stock Price')

## splitting the required matrix
X = df.iloc[:,:-1]

## Finding mean and median for the price 
mean_X = statistics.mean(X.iloc[:,3])
median_X = statistics.median(X.iloc[:,3])

print("Mean Price :",mean_X)
print("Median Price :",median_X)

## Finding the sample mean of price for wednesdays 

wed_rows = X[X['Day'] == "Wed"]
wed_prices = wed_rows['Price'].astype(float)

wed_mean = statistics.mean(wed_prices)

print("Wednesday price mean :",wed_mean)
print("Difference :", wed_mean-mean_X)

## Finding the sample mean of price for April

april_rows = X[X['Month'] == "Apr"]
april_prices = april_rows['Price'].astype(float)

april_mean = statistics.mean(april_prices)

print("April prices mean :",april_mean)
print("Difference :",mean_X-april_mean)