import requests
import pandas as pd

def collect_data():
    # Example: Collect data from an API
    response = requests.get('https://api.example.com/data')
    data = response.json()

    # Example: Store data in a CSV file
    df = pd.DataFrame(data)
    df.to_csv('data/collected_data.csv', index=False)

if __name__ == '__main__':
    collect_data()
