import numpy as np  ## for matrices 
import pandas as pd ## for importing xlxs  
from sklearn.preprocessing import MinMaxScaler ## for normalization

## loading the required sheet 
file_path = "/Users/niteshnirranjan/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='marketing_campaign')
df = df.iloc[:,9:]

## applying normalization 
scaler = MinMaxScaler()
norm_data = scaler.fit_transform(df)
print(norm_data)