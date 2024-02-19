import matplotlib.pyplot as plt
import pandas as pd

def visualize_data(data):
    """
    Visualize data from the processed dataset.
    
    Args:
        data (pandas.DataFrame): The processed dataset.
    """
    # Choose the column for visualization (e.g., 'Rate of individuals with zero components of social vulnerability')
    column_to_visualize = 'Rate of individuals with zero components of social vulnerability'
    
    # Plot the distribution of the selected column
    plt.figure(figsize=(8, 6))
    data[column_to_visualize].hist(bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Social Vulnerability Rates')
    plt.xlabel('Social Vulnerability Rate')
    plt.ylabel('Frequency')
    plt.grid(False)
    plt.show()

if __name__ == '__main__':
    # Load the processed dataset (assuming 'processed_data' is already loaded)
    processed_data = pd.read_csv('data/CRE2022.CRE-Data.csv')  # Adjust the file path as needed
    visualize_data(processed_data)
