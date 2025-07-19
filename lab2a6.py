import numpy as np  ## for matrices 
import pandas as pd ## for importing xlxs  
from sklearn.preprocessing import LabelEncoder ## for encoding values 
from sklearn.metrics.pairwise import cosine_similarity ## for computing jacquard coefficient 


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

## Computing cosine similarity 
cos_sim = cosine_similarity([X],[Y]) 
print("Cosine Similarity :",cos_sim)

