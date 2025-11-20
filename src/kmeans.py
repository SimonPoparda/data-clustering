from abc import ABC, abstractmethod
import pandas as pd
import numpy as np

class BaseClustering(ABC):
    """Abstract class for clustering models"""

    @abstractmethod
    def fit(self, X: pd.DataFrame):
        """Fit the model to the data."""
        pass

    @abstractmethod
    def predict(self, X: pd.DataFrame):
        """Predict cluster labels for new data points."""
        pass

class KMeansCustom(BaseClustering):
    """KMeans with standard random initialization from data points."""

    def __init__(self, k: int):
        self.k = k                
        self._centroids = None      
        self._labels = None       
        self.n_iterations = 0       

    @property
    def centroids(self):
        """Getter for centroids"""
        return self._centroids

    @property
    def labels(self):
        """Getter for cluster labels"""
        return self._labels

    @property
    def iterations(self):
        """Getter for number of iterations of the model"""
        return self.n_iterations
    
    def fit(self, X: pd.DataFrame):
        """Method that trains the model by finding the centroids""" 
        X = X.to_numpy()
        n_samples = X.shape[0]

        random_generator = np.random.default_rng()
        indexes = random_generator.choice(n_samples, self.k, replace=False)
        self._centroids = X[indexes]

        while True:
            # return the distances from each centroid
            distances = np.linalg.norm(X[:, np.newaxis] - self._centroids, axis=2)
            
            # assign each data point to the nearest label of the nearest centroid 
            # label will be the index of the centroid in the list
            labels = np.argmin(distances, axis=1)

            #calculate the average for data points with the same label
            new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])

            self.n_iterations += 1

            # compare new_centroids to the previous centroids to check if they changed or not with tolerance
            if np.allclose(self._centroids, new_centroids):
                break

            self._centroids = new_centroids
            self._labels = labels

    def predict(self, X: pd.DataFrame):
        """Method that will assign the labels to new data points"""
        
        if self._centroids is None:
            raise ValueError('Model must be fitted before calling predict')
        
        X = X.to_numpy()

        #calculate the distance from new data point to the centroids
        distances = np.linalg.norm(X[:, np.newaxis] - self._centroids, axis=2)

        # return the centroid's indexes as labels for each data point
        return np.argmin(distances, axis=1)

