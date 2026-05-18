from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_files(
    "bisesh08/kathmandu-aqi-dataset-2023-2024",
    path="../data/raw",
    unzip=True
)