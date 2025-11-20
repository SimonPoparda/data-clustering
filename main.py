from src.data_loader import load_data
from src.data_cleaner import DataCleaner
from src.data_inputer import ClusterInput
from src.kmeans import KMeansCustom
from src.plotter import plot_clusters

if __name__ == "__main__":
    loaded_df = load_data(r"data/IRIS.csv")
    cleaner = DataCleaner(loaded_df)

    full_df, numeric_df = cleaner.clean()  # performs data cleaning

    input_handler = ClusterInput()
    k = input_handler.get_user_input()  # sets number of clusters

    model1 = KMeansCustom(k)
    model1.fit(numeric_df)  # trains the model
    model1.predict(numeric_df)  # predicts the labels

    plot_clusters(numeric_df, model1.labels, model1.centroids)  # plot the results
