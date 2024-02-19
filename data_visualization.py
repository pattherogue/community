import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a pandas DataFrame
file_path = "/path/to/your/dataset/CRE2022.CRE-Data.csv"
df = pd.read_csv(file_path)

# Visualize the rate of individuals with zero components of social vulnerability
sns.histplot(df['Rate of individuals with zero components of social vulnerability'], kde=True)
plt.title("Distribution of Rate of Individuals with Zero Components of Social Vulnerability")
plt.xlabel("Rate")
plt.ylabel("Frequency")
plt.show()
