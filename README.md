# Market Basket Analysis

This is a simple implementation of a market basket analysis problem. Here, we assume we work for a
retail company specialized in food products.

The dataset used in this project in this project comes from the [Groceries Market Basket Dataset](https://www.kaggle.com/datasets/irfanasrullah/groceries) on Kaggle. In this project, the dataset is versioned with [DVC](https://dvc.org/), using Dagshub as a remote. You can find the Dagshub repo of this project [here](https://dagshub.com/ericdasse28/market-basket-analysis)

If you wanna learn how to use DVC, you can get started with [this tutorial](https://dvc.org/doc/start).

---
**Note**

You might find a Google Drive remote among the remotes of this project and also see `dvc-gdrive` in the requirements. This is simply because Google Drive was used as a remote in the early stages of the project for the sake of experimenting.

---

## Project structure

- `code/`: all source code
    * `ml_training/process_data.py`: data preparation code
    * `ml_training/train.py`: ML training
    * `ml_app/app.py`: simple Flask app to serve ML model (ML application)

- `data/`: data used or produced by the ML pipeline
    * `raw`: raw CSV data coming from aformentioned Kaggle dataset. It needs to be renamed `groceries.csv`
    * `prepared`: where the processed CSV file is stored

- `model/`: Location of the model

## Getting started


## Running the ML training
The training is automatically run in the GitHub Actions workflow named _ML pipeline_ every time there is an update on the data or the training code in `code/ml_training` on the master branch.

Additionally, you can run it locally either by running the DVC pipeline with the following command

```sh
$ dvc repro
```

or doing it manually step by step
```sh
$ python code/ml_training/process_data.py # If it's not already done
$ python code/ml_training.train.py
```

Either way, it generates a model that is serialized, stored in the `model/` directory and then versioned/to be versioned by DVC. When the training is done by the GitHub Actions workflow, it takes care of versioning the model itself and even committing the changes to `dvc.lock` if necessary.

The DVC remote is used as a model registry. When we serve the model, we import it from that DVC remote

## ML application
A simple Flask application was made to serve the model through API calls. The app code is located at `code/ml_app/`

 The app is deployed in a docker image that can be found in this [Docker Hub](https://github.com/ericdasse28/market-basket-analysis).

Once the app is running, you can obtain a prediction of the next product that could be bought given a product sent to the API as input
