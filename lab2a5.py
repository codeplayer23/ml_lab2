import numpy as np  ## for matrices 
import pandas as pd ## for importing xlxs  
from sklearn.preprocessing import LabelEncoder ## for encoding values 
from sklearn.metrics import jaccard_score , confusion_matrix ## for computing jacquard coefficient 


## loading the required sheet 
file_path = "/Users/niteshnirranjan/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='thyroid0387_UCI')
 
## Taking first two observations 
X = df.iloc[1,4:18]
Y = df.iloc[2,4:18]

## encoding values 
le = LabelEncoder()
X = le.fit_transform(X)
Y = le.fit_transform(Y)

## Computing jacquard coeefficient 
print("JC:",jaccard_score(X,Y))

## Computing Simple Matrix Coefficient

matches = sum([1 for a, b in zip(X,Y) if a == b])
smc = matches / len(X)
print("SMC:", smc)
