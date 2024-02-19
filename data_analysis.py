import pandas as pd

def explore_data(data):
    """
    Perform exploratory data analysis (EDA) on the dataset.
    
    Args:
        data (pandas.DataFrame): The dataset to analyze.
    """
    # Perform exploratory data analysis here
    # Example: Display summary statistics
    print(data.describe())
    
    # Example: Visualize distributions
    # import matplotlib.pyplot as plt
    # data.hist(figsize=(10, 10))
    # plt.show()

# Example usage
if __name__ == "__main__":
    # Assuming 'data' is already loaded from data_collection.py
    explore_data(data)
