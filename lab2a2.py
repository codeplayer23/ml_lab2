import numpy as np  ## for matrices 
import pandas as pd ## for importing xlxs  

## loading the required sheet 
file_path = "/Users/niteshnirranjan/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='Purchase data')

## Segregating into two different matrices 
A = df.iloc[:,0].values
C = df.iloc[:,4].values

## classifying the customers as RICH or POOR 
status_array = np.where(C>=200 , 'RICH' , 'POOR')
print(status_array)