import requests
import json
import pandas as pd

df = pd.read_csv('Output.csv')

processed_data = df.to_dict(orient='records')

api_url = "http://localhost:3000/api/data"
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(api_url, data=json.dumps(processed_data), headers=headers)
    response.raise_for_status()
    print("Data successfully sent to the API.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")