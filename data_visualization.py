import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(data):
    """
    Visualize a numeric column from the dataset using a histogram.
    
    Args:
        data (pandas.DataFrame): The dataset containing the column to visualize.
    """
    # Replace 'YourNumericColumn' with the name of the correct column
    column_to_visualize = 'PRED0_PE'
    
    # Check if the column exists in the dataset
    if column_to_visualize not in data.columns:
        print(f"Column '{column_to_visualize}' not found in the dataset.")
        return
    
    # Plot a histogram of the selected column
    plt.figure(figsize=(10, 6))
    data[column_to_visualize].hist(bins=320, color='skyblue', edgecolor='black')
    plt.xlabel(column_to_visualize)
    plt.ylabel('Frequency')
    plt.title('Histogram of ' + column_to_visualize)
    plt.grid(False)
    plt.show()

if __name__ == "__main__":
    # Load the processed dataset
    processed_data = pd.read_csv('data/CRE2022.CRE-Data.csv')  # Adjust the file path as needed
    
    # Visualize the selected column
    visualize_data(processed_data)
