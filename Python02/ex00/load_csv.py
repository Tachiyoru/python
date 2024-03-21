import pandas as pd
# import numpy as np

def load(path: str):
    """
    Load a CSV file as a pandas DataFrame.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame or None: The loaded DataFrame if successful, None otherwise.
    """
    try:
        # data = np.genfromtxt(path, delimiter=',')
        # on ne peut pas utiliser numpy car en cas de manquement de valeur numpy leve une erreur
        # tandis que pandas la remplace par NaN
        
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data

    except FileNotFoundError:
        print("The file path provided does not exist.")
        return None
    except pd.errors.ParserError:
        print("There was a problem parsing the file.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    

def main():
    print(load("life_expectancy_years.csv"))
    return


if __name__ == "__main__":
    main()