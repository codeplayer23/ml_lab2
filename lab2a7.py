import numpy as np  ## for matrices 
import pandas as pd ## for importing xlxs  
from sklearn.preprocessing import LabelEncoder ## for encoding values 
from sklearn.metrics import jaccard_score  ## for computing Jaccard Coefficient
from sklearn.metrics.pairwise import cosine_similarity ## for computing cosine similarity

# Loading the required sheet 
file_path = "/Users/niteshnirranjan/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='thyroid0387_UCI')
 
# Taking first 20 observations 
X = df.iloc[:20, 4:18]
Y = df.iloc[:20, 4:18]

# Encoding each column separately
le = LabelEncoder()
for col in X.columns:
    X[col] = le.fit_transform(X[col])
    Y[col] = le.fit_transform(Y[col])

# Selecting two individual samples 
x1 = X.iloc[0].to_numpy()
y1 = Y.iloc[1].to_numpy()

# Computing Jaccard Coefficient 
print("JC:", jaccard_score(x1, y1, average='macro'))

# Computing Simple Matching Coefficient
matches = np.sum(x1 == y1)
smc = matches / len(x1)
print("SMC:", smc)

# Computing Cosine Similarity 
cos_sim = cosine_similarity([x1], [y1]) 
print("Cosine Similarity :", cos_sim)
