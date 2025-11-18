import numpy as np
import pandas as pd
import random

class KMeansCustom:
    def __init__(self, n_clusters: int = 3, max_iter: int = 100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self._centroids = None

    @property
    def centroids(self):
        return self._centroids
    
    def _initialize_centroids(self, X: pd.DataFrame):
        self._centroids = X.sample(self.n_clusters).to_numpy()

    def _assign_clusters(self, X: pd.DataFrame) -> list[int]:
        clusters = []
        for _, row in X.iterrows():
            distances = np.linalg.norm(row.to_numpy() - self._centroids, axis=1)
            cluster_id = int(np.argmin(distances))
            clusters.append(cluster_id)
        return clusters
    
    def _update_centroids(self, X: pd.DataFrame, clusters: list[int]) -> np.ndarray:
        new_centroids = []
        for cluster_idx in range(self.n_clusters):
            cluster_points = X[np.array(clusters) == cluster_idx]
            if len(cluster_points) == 0:
                # pusty klaster → losujemy nowy centroid
                new_centroids.append(X.sample(1).to_numpy()[0])
            else:
                new_centroids.append(cluster_points.mean().to_numpy())
        return np.array(new_centroids)
    
    def fit(self, X: pd.DataFrame) -> list[int]:
        self._initialize_centroids(X)

        for iteration in range(self.max_iter):
            clusters = self._assign_clusters(X)
            new_centroids = self._update_centroids(X, clusters)

            # warunek stopu
            if np.allclose(self._centroids, new_centroids):
                print(f"Konwergencja po {iteration} iteracjach")
                break

            self._centroids = new_centroids

        return clusters


    