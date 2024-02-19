import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

def visualize_data():
    # Example: Read data from CSV file
    df = pd.read_csv('data/collected_data.csv')

    # Example: Create a bar plot using matplotlib
    plt.bar(df['Category'], df['Value'])
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.title('Data Visualization')
    plt.show()

    # Example: Create an interactive scatter plot using Plotly
    fig = px.scatter(df, x='X', y='Y', color='Category', title='Interactive Plot')
    fig.show()

if __name__ == '__main__':
    visualize_data()
