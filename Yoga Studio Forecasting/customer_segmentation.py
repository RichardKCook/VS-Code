import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load demographic data
df = pd.read_csv('demographic_data.csv')

# Example demographic data for clustering
df['age'] = [25, 35, 45, 55, 65, 30, 40, 50, 60, 70]
df['income'] = [50000, 60000, 70000, 80000, 90000, 52000, 62000, 72000, 82000, 92000]

X = df[['age', 'income']]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
df['segment'] = kmeans.labels_

# Save the segmented data
df.to_csv('segmented_data.csv', index=False)

# Plot the clusters
plt.scatter(df['age'], df['income'], c=df['segment'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Customer Segmentation')
plt.savefig('customer_segmentation.png')
plt.show()
