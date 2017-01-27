# K-means clustering

The procedure with K-means is:

1 Choose the number of clusters, K
2 Select at random the K points to be initial centroids (not necessarily from dataset)
3 Assign each datapoint to the closest (e.g. euclidean distance metric) centroid to fall under that cluster
4 Compute and place the new centroid of each cluster as the mean point of the cluster
5 Reassign each datapoint to the new closest centroid. If there was a reassignment go back to 4. Otherwise we're complete.

The K points in step 2 are not just selected at random in a non-restricted way in the example as the example is actually using K-means++, which is an enhancement because random selection could lead to different results. The library does that for us.

The optimal number of clusters can be decided by considering the way that the total 'error' or WCSS (within cluster sum of squares - total squared distance of points to their centroids) drops off as number of clusters increases. The elbow method means taking the point at which the WCSS reduction slows down and uses that as the number of clusters. We do this in the example by plotting the WCSS against the number of clusters and choosing a value i.e. by inspecting the graph. 

The example is a market segmentation exercise. We are only using two variables from the data - the last two columns Annual Income and Spending Score.

There's no test and training split as this is unsupervised learning, we don't have labels