import requests

url = "http://localhost:8000/fastAPI2"
payload = {"text": "I love this product!"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.json())