import numpy as np  ## for matrices 
import pandas as pd ## for importing xlxs  
from sklearn.preprocessing import OneHotEncoder , LabelEncoder

## loading the required sheet 
file_path = "/Users/niteshnirranjan/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='thyroid0387_UCI')

## replacing missing values with nan to not interfere with numerical values computations 
df.replace("?", np.nan, inplace=True)

## loading the data matrix 
referral_s = df["referral source"] 
gender = df["sex"]
condition = df["Condition"]

## applying lable encoder for sex
le = LabelEncoder()
gender_encoded = le.fit_transform(gender)
print(gender_encoded)

## applying lable encoder for referral source
referral_s_encoded = le.fit_transform(referral_s)
print(referral_s_encoded)

## applying one hot encoding for condition
one_hot = pd.get_dummies(condition)
print(one_hot)

## Studying the range of values 
age = df["age"]
age_range = age.max() - age.min()  
print("Range of age :",age_range)

tsh = df["TSH"]
tsh_range = tsh.max() - tsh.min()
print("Range of TSH values :",tsh_range)

t3 = df["T3"].dropna()
t3_range = t3.max() - t3.min()
print("Range of T3 values :",t3_range)

tt4 = df["TT4"].dropna()
tt4_range = tt4.max() - tt4.min()
print("Range of TT4 values :",tt4_range)

t4u = df["T4U"].dropna()
t4u_range = t4u.max() - t4u.min()
print("Range of T4U values :",t4u_range)

fti = df["FTI"].dropna()
fti_range = fti.max() - fti.min()
print("Range of FTI values :",fti_range)

tbg = df["TBG"].dropna()
tbg_range = tbg.max() - tbg.min()
print("Range of TSH values :",tbg_range)

##finding mean and variance for the numerical values 
mean_age = age.mean()
var_age = age.var()
print("Mean age :" , mean_age)
print("Variance of age :",var_age)

mean_tsh = tsh.mean()
var_tsh = tsh.var()
print("Mean TSH :",mean_tsh)
print("Variance of TSH :",var_tsh)

mean_t3 = t3.mean()
var_t3 = t3.var()
print("Mean of T3 :",mean_t3)
print("Variance of T3 :",var_t3)

mean_tt4 = tt4.mean()
var_tt4 = tt4.var()
print("Mean of TT4 :",mean_tt4)
print("Variance of TT4 :",var_tt4)

mean_t4u = t4u.mean()
var_t4u = t4u.var()
print("Mean of T4U :",mean_t4u)
print("Variance of T4U :",var_t4u)

mean_fti = fti.mean()
var_fti = fti.var()
print("Mean of FTI :",mean_fti)
print("Variance of FTI :",var_fti)

mean_tbg = tbg.mean()
var_tbg = tbg.var()
print("Mean of TBG :",mean_tbg)
print("Variance of TBG :",var_tbg)

