from src.data_loader import load_data
from src.data_cleaner import DataCleaner
from src.data_inputer import Inputer, MockDataGenerator
from src.kmeans import KMeansCustom
from src.plotter import plot_clusters

if __name__ == "__main__":
    loaded_df = load_data(r'data/IRIS_test.csv')
    mock_data_destination = r'data/IRIS_mock.parquet'
    cleaner = DataCleaner(loaded_df)

    full_df, numeric_df_test = cleaner.clean()  # perform data cleaning
    
    input_handler = Inputer()
    n_rows = input_handler.get_user_input('Podaj liczbę wierszy do wygenerowania: ') # sets number of rows to generate

    mock_data_generator = MockDataGenerator(numeric_df_test) 
    mock_data_generator.generate_and_write_mock_df(n_rows, mock_data_destination)
    
    k = input_handler.get_user_input('Podaj liczbę klastrów: ')  # sets number of clusters

    model = KMeansCustom(k) 
    model.fit(numeric_df_test)  # trains the model
    labels_mock = model.predict(mock_data_generator.mock_df)  # predicts the labels

    plot_clusters(numeric_df_test, model.labels, model.centroids)