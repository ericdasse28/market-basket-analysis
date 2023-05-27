import os
from pathlib import Path
from typing import List
from loguru import logger
import pandas as pd


def save_transactions_as_csv(list_transactions: List[list], path_to_csv: os.PathLike):
    with open(path_to_csv, "wb") as csvfile:
        for transaction in list_transactions:
            row = ",".join(transaction)
            row = f"{row}\n".encode()
            csvfile.write(row)


def process_data():
    logger.info("Préparation de données en cours...")

    logger.info("Récupération des données brutes")
    repo_path = Path(__file__).parent.parent
    data_path = repo_path / "data/raw/groceries.csv"
    sales_df = pd.read_csv(data_path)

    logger.info("Groupement en transactions")

    transactions = sales_df.groupby(["Member_number", "Date"])
    list_transactions = [
        transaction[1]["itemDescription"].tolist() for transaction in list(transactions)
    ]

    logger.info("Sauvegarde des données préparées...")
    prepared_file = repo_path / "data/prepared/prepared.csv"
    save_transactions_as_csv(list_transactions, path_to_csv=prepared_file)

    logger.info("Préparation terminée.")


if __name__ == "__main__":
    process_data()
