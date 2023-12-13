import pandas as pd

# Loading dataframes
df1 = pd.read_csv("D:\MDS_UPDRS_Part_I.csv")
df2 = pd.read_csv("D:\MDS_UPDRS_Part_II.csv")
df3 = pd.read_csv("D:\MDS_UPDRS_Part_III.csv")
df4 = pd.read_csv("D:\MDS_UPDRS_Part_IV.csv")
df5 = pd.read_csv("D:\MDS1.csv")
df6 = pd.read_csv("D:\MDS-UPDRS_Tagging.csv")

# Combine two dataframes =================== Behzad Amanpour ==================
df_combined = pd.merge(df1, df2, on = ['PATNO', 'EVENT_ID'], how = "outer") # inner

df_filtered = df_combined[ df_combined['EVENT_ID'] == "BL" ]

new_cols = df2.columns.difference( df1.columns )

new_cols = new_cols.append( pd.Index(['PATNO', 'EVENT_ID']) )

df_combined2 = pd.merge(df1, df2[new_cols], on = ['PATNO', 'EVENT_ID'], how = "outer")

df_filtered2 = df_combined2[ df_combined2['EVENT_ID'] == "BL" ]

df_filtered2 = df_filtered2.dropna( axis=1, how= 'all' )  

df_filtered2 = df_filtered2.dropna( axis=0, how= 'all' ) 

# Combine multiple dataframes ============== Behzad Amanpour ==================
# list of the DataFrames
dfs = [df2, df3, df4, df5, df6]
# Initialize the combined DataFrame
df_combined = df1

# Loop over the DataFrames two by two
for i in range(len(dfs)): # i=0
    new_cols = dfs[i].columns.difference(df_combined.columns)
    new_cols = new_cols.append(pd.Index(['PATNO', 'EVENT_ID']))
    df_combined = pd.merge(df_combined, dfs[i][new_cols], on=['PATNO', 'EVENT_ID'], how="outer")
    
# Filtering "EVENT_ID"="BL"
df_filtered = df_combined[df_combined['EVENT_ID'] == "BL"]

df_filtered2 = df_filtered.dropna( axis=1, how= 'all' ) #  , 'any'

thresh = len(df_filtered) * 0.5

df_filtered3 = df_filtered.dropna( axis=1, thresh = thresh )

df_filtered3.to_csv('D:\Result.csv')
