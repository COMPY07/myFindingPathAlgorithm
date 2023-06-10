from sklearn.neighbors import KNeighborsClassifier

x = [[0],[1],[2],[3]]
y = [0, 0, 1, 1]
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x, y)
print(neigh.predict([[1.1]]))
