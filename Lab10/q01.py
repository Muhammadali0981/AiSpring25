# Lab10 Task 1: Data Loading and Preprocessing

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
# (Assumes 'Mall_Customers.csv' is in the same directory)
df = pd.read_csv('Mall_Customers.csv')

# Show info and head (for script, you may use print or comment out)
df.info()
df.head()

# Describe the data
df.describe()

# Drop the CustomerID column
df.drop('CustomerID', axis=1, inplace=True)

# Encode the Gender column as numeric
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# The dataframe 'df' is now preprocessed for further analysis or clustering.
