from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.data_inputer import get_user_input
from src.kmeans import KMeansCustom

if __name__ == '__main__':
    loaded_df = load_data(r'data/IRIS.csv')

    full_df, numeric_df = clean_data(loaded_df)

    k = get_user_input()

    model = KMeansCustom(n_clusters=k)
    clusters = model.fit(numeric_df)

    print("Centroidy:")
    print(model.centroids)
    print("Przypisane klastry:")
    print(clusters)


    