import pandas as pd
# from pandas import read_excel, get_dummies
import numpy as np

df = pd.read_excel ('D:\patients_missing.xlsx')
df_missed = df[ df.isnull().any(axis=1) ]

# Categorical to Numerical
df['Gender'].replace(['Male', 'Female'], [1, 0], inplace=True)

df = pd.get_dummies( df, columns=['Gender'], drop_first=True, dummy_na=True) # 
df.loc[ df['Gender_nan']==1, 'Gender_Male' ] = np.nan
df = df.drop( ['Gender_nan'], axis=1 )

X = df.values

# KNN Imputer ================== Behzad Amanpour ==============================
from sklearn.impute import KNNImputer
Imputer = KNNImputer() # n_neighbors = 3
X2 = Imputer.fit_transform( X ) 
df_KNN = pd.DataFrame( X2, columns = df.columns)

# IterativeImputer ============= Behzad Amanpour ==============================
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
Imputer = IterativeImputer() # random_state=0
X3 = Imputer.fit_transform( X )
X3 = np.round( Imputer.fit_transform( X ) )
df_Iterative = pd.DataFrame( X3, columns = df.columns)
