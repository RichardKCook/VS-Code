import requests
import pandas as pd

# Your U.S. Census API key
api_key = 'YOUR_API_KEY'

# Define the API endpoint and parameters
endpoint = 'https://api.census.gov/data/2020/dec/pl'
params = {
    'get': 'NAME,P1_001N',  # Total population
    'for': 'tract:*',
    'in': 'state:06 county:075',  # Example: California, San Francisco County
    'key': api_key
}

# Make the request to the Census API
response = requests.get(endpoint, params=params)

# Convert the response to a DataFrame
data = response.json()
columns = data[0]
rows = data[1:]
df = pd.DataFrame(rows, columns=columns)

# Save the data to a CSV file
df.to_csv('demographic_data.csv', index=False)
