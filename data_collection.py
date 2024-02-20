import pandas as pd

def load_data(file_path):
    """
    Load the dataset into a pandas DataFrame.
    
    Parameters:
        file_path (str): The path to the dataset file.
    
    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    df = pd.read_csv(file_path)
    return df
