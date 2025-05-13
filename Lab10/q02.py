from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Mall_Customers.csv')
df.drop('CustomerID', axis=1, inplace=True)

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])


sns.heatmap(df.select_dtypes(include="number").corr())
plt.show()


wcss = []
for i in range(1, 11):
    model = KMeans(i, init='k-means++', random_state=727)
    model.fit(df)
    wcss.append(model.inertia_)

sns.lineplot(wcss)
plt.show()


def kmeans(data, k=5, rs=727):
    model = KMeans(k, init='k-means++', random_state=rs)
    return model.fit_predict(data)

df_ohne_age = df.drop('Age', axis=1)
ss = StandardScaler()
df_scaled = ss.fit_transform(df_ohne_age)

predictions_normal = kmeans(df_ohne_age)
predictions_scaled = kmeans(df_scaled) 