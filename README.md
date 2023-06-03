# Market Basket Analysis

This is a simple implementation of a market basket analysis problem. Here, we assume we work for a
retail company specialized in food products.

The dataset used in this project in this project comes from the [Groceries Market Basket Dataset](https://www.kaggle.com/datasets/irfanasrullah/groceries) on Kaggle. It is versioned with [DVC](https://dvc.org/).

## Project structure

- `src/`: source code
    * `process_data.py`: data preparation code
    * `train.py`: ML training
    * `app.py`: simple Flask app to serve ML model

- `data/`: data used or produced by the ML pipeline
    * `raw`: raw CSV data coming from aformentioned Kaggle dataset. It needs to be renamed `groceries.csv`
    * `prepared`: where the processed CSV file is stored

- `model/`: Location of the model