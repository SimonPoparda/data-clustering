import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_clusters(X: pd.DataFrame, labels: np.ndarray, centroids: np.ndarray):
    col1, col2 = X.columns[0], X.columns[1]

    X = X.to_numpy()

    plt.scatter(
        X[:, 0],
        X[:, 1],
        c=labels,
        s=30,
        alpha=0.7
    )

    plt.scatter(
        centroids[:, 0],
        centroids[:, 1],
        marker="X",
        s=200,
        edgecolors="black"
    )

    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title("Wynik klasteryzacji (KMeansCustom)")
    plt.show()


