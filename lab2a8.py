import numpy as np  ## for matrices 
import pandas as pd ## for importing xlxs  

## loading the required sheet 
file_path = "/Users/niteshnirranjan/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='thyroid0387_UCI')

## making "?" as nan
df.replace("?", np.nan, inplace=True)


## filling in missing values for income 
df["TSH"].fillna(df["TSH"].median(), inplace=True)
print(df["TSH"])

