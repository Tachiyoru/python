import pandas as pd
import sys
# import numpy as np


def load(path: str):
    """
    Load a CSV file as a pandas DataFrame.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame or None: The loaded DataFrame if successful,
            None otherwise.
    """
    try:
        # data = np.genfromtxt(path, delimiter=',')
        # on ne peut pas utiliser numpy car en cas de manquement de valeur
        # numpy leve une erreur
        # tandis que pandas la remplace par NaN

        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(type(e).__name__ + ":", e)
        sys.exit(1)


def main():
    print(load("life_expectancy_years.csv"))
    return


if __name__ == "__main__":
    main()
