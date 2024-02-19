import pandas as pd

# Define the full file path
file_path = "/Users/paologomez/Downloads/CRE2022.CRE_2024-02-19T170945"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())
