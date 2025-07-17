import requests

url = "http://localhost:8000/fastAPI1"
payload = {"text": "I love coding and running!"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.json())