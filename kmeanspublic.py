import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans

dataset =pd.read_csv('cars.csv')
x = dataset.iloc[: ,[1,2]].values
print(x)

wcss = []

for i in range(1, 11):
 kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
 kmeans.fit(x)
 wcss.append(kmeans.inertia_)

mtp.plot(range(1, 11),wcss)
mtp.xlabel('number of clusters')
mtp.ylabel('wcss')
mtp.show()

kmeans = KMeans(n_clusters=5, init="k-means++", random_state=42)
y_kmeans = kmeans.fit_predict(x)
mtp.scatter(x[y_kmeans==0,0], x[y_kmeans==0,1], s=80, c='red', label = 'Cluster 1')
mtp.scatter(x[y_kmeans==1,0], x[y_kmeans==1,1], s=80, c='blue', label = 'Cluster 2')
mtp.scatter(x[y_kmeans==2,0], x[y_kmeans==2,1], s=80, c='green', label = 'Cluster 3')
mtp.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c ='black', label = 'Centroids')
mtp.legend()
mtp.show()