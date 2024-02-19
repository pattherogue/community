import pandas as pd

def load_data(file_path):
    """
    Load the dataset into a pandas DataFrame.
    
    Args:
        file_path (str): The file path to the CSV dataset.
    
    Returns:
        pandas.DataFrame: The loaded dataset.
    """
    # Load the dataset into a DataFrame
    df = pd.read_csv(file_path)
    
    return df

# Example usage
if __name__ == "__main__":
    file_path = "data/CRE2022.CRE-Data.csv"
    data = load_data(file_path)
    print(data.head())
