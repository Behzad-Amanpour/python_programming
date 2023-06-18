"""
Please scroll down for "Missing Values Interpolation"
"""

import pandas as pd

# Reading an excel file to a dataframe -----------------------------------------
df = pd.read_excel ('address\file_name.xlsx')

# Replacing categorical values with numerical ----------------------------------
df['Status'].replace(['Excellent', 'Good', 'Fair', 'Poor'], [1, 1, 0, 0], inplace=True)

# Replacing categorical values with dummy variables ----------------------------
df3 = pd.get_dummies(df, columns=['Location', 'Gender', 'Smoker'], drop_first=True)

# Removing a column from dataframe ---------------------------------------------
df3.drop(['LastName'], inplace=True, axis=1) 

# Exporting values of a dataframe columns --------------------------------------
X = df3[['Age', 'Height', 'Weight', 'Systolic','Diastolic', "Location_STM",
         'Location_VA', 'Gender_Male','Smoker_True']].values

# Checking for missing values --------------------------------------------------
df2 = df.isnull()   # df2 is a boolean same-sized dataframe, with "True" for "NaN" values and "False" for the others
rows, cols = np.where(df2)  # you get the row and column indexes of null/NaN values

df_row = df[df.isnull().any(axis=1)]  # you get rows of "df" with null values
df_row2= df[df["Smoker"].isnull()]   # you get rows of "df" where values of the column "Smoker" are null/NaN

# Filling missing values in ---------------------------------------------------
df2 = df.fillna(0)                 # filling "NaN" values with zero
df2 = df.fillna( method ='pad' )   # filling "NaN" values with the value from the last row
df2 = df.fillna( method ='bfill' ) # filling "NaN" values with the value from the next row
df2 = df.fillna('no value')
df2["Gender"] = df["Gender"].fillna('No Gender')  # replaces all "NaN" values in the column "Gender" with "No Gender"
df2["Smoker"] = df["Smoker"].fillna(0)

# Dropping NaN Values ---------------------------------------------------------
df2 = df.dropna()            # drops all rows with one or more missing values
df2 = df.dropna(axis = 1)    # drops all columns with one or more missing values
df2 = df.dropna(how = 'all') # drops rows with all values missed


# Missing Values Interpolation ----------------------- Behzad Amanpour -------
"""
We need to interpolate the missing values of two columns "Gender" & "Blood_pressure" in our data frame "df"
"""
# ---------------------------------------------------- Behzad Amanpour -------

# Correlation matrix of the dataframe "df"
Corr = df.corr()

# Interpolation of categirical variable "Gender"
df = df.sort_values(['Weight'])     # We sort the df rows based on "Weight" which has high correlation with "Gender"
df[ "Gender" ] = df[ "Gender" ].interpolate( method ='pad', limit=2)

# Interpolation of numerical variable "Blood_pressure"
df = df.sort_values(['Smoker'])     # We sort the rows of "df" based on its column "Smoker" which has high correlation with "Blood_pressure"
df[ "Blood_pressure" ] = df[ "Blood_pressure" ].interpolate( method ='linear', limit=2)

# Multiple Samples Average 
import numpy as np
def average3( array, ix):
    return round( array[ix-3]+ array[ix-2]+ array[ix-1]+ array[ix+1]+ array[ix+2]+ array[ix+3] ) / 6 )
           # you might not need the round() function
n = 3
def average_n( array, ix):
    return round( (np.sum(array[ix-n : ix+n+1]) - array[ix]) / (n*2) )
           # you might not need the round() function

values = df['Blood_pressure'].values
values = np.nan_to_num(values, nan=999)
for i in range( np.shape( values )[0] ): 
    if values[i] == 999:  # and i > 2
        values[i] = average3( values, i )   # average_n( values, i )
        print(i)
df['Blood_pressure'] = values
