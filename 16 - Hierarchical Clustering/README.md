# Hierarchical Clustering

Agglomerative hierarchical clustering follows these steps:

1 Make each data point a cluster so that you have the same number of clusters as data points.
2 Take the two closest data points and make them one cluster.
3 Take the two closest clusters (a single data point is also a cluster) and make them one cluster.
4 Repeat step 3 until there is only one cluster.

Each of the stages of agglomeration are stored in a dendrogram (https://en.wikipedia.org/wiki/Dendrogram). The dendrogram records the distances between each of the clusters when they were merged. So one way to decide the number of clusters is to choose a threshold on distance for the merging step.

Closest clusters can be defined in different ways (by centroid distances, nearest points, furthest points etc.). This is something that can vary across implementations but isn't a focus here.

Example uses same data set as last example.

Also included is a comparison of different clustering techniques.