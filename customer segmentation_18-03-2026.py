from sklearn.cluster import KMeans

# Customer data (Income, Spending Score)
data = [
    [15, 39],
    [16, 81],
    [17, 6],
    [18, 77],
    [19, 40],
    [20, 76]
]

# Apply K-Means
kmeans = KMeans(n_clusters=2)

kmeans.fit(data)

# Show cluster results
print("Customer Groups:")
print(kmeans.labels_)