from pathlib import Path
import pickle
from loguru import logger
import pandas as pd
from apyori import apriori


def read_transaction_csv(csv_path):
    with open(csv_path, "r") as transaction_csv:
        list_transactions = transaction_csv.readlines()
        list_transactions = map(lambda row: row.split(","), list_transactions)

        return list_transactions


def inspect(results):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    support = [result[1] * 100 for result in results]
    confidence = [result[2][0][2] for result in results]
    lift = [result[2][0][3] for result in results]

    return list(zip(lhs, rhs, support, confidence, lift))


def learn_association_rules():
    repo_path = Path(__file__).parent.parent
    prepared_data_path = repo_path / "data/prepared/prepared.csv"
    transactions = read_transaction_csv(prepared_data_path)

    # list_transactions = [
    #     transaction[1]["itemDescription"].tolist() for transaction in list(transactions)
    # ]

    association_rules = apriori(
        transactions,
        min_support=0.001,
        min_confidence=0.05,
        min_lift=1.2,
        min_length=2,
        max_length=2,
    )

    association_results = list(association_rules)
    association_df = pd.DataFrame(
        inspect(association_results),
        columns=["Product1", "Product2", "Support (%)", "Confidence (%)", "lift"],
    )
    association_df["Rule"] = association_df[["Product1", "Product2"]].apply(
        lambda row: "->".join(row.values.astype(str)), axis=1
    )

    return association_df


def train(serialize=True):
    logger.info("Début de l'entraînement...")
    association_rules_df = learn_association_rules()
    logger.info("Entraînement terminé.")

    logger.info(f"Aperçu des règles d'association\n{association_rules_df.head()}")

    if serialize:
        logger.info("Sérialisation du modèle...")
        repo_path = Path(__file__).parent.parent
        model_save_path = repo_path / "model/association_rules.pkl"

        with open(model_save_path, "wb") as association_rules_file:
            pickle.dump(association_rules_df, file=association_rules_file)

        logger.info("Modèle sérialisé.")


if __name__ == "__main__":
    train()
