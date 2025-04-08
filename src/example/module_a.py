import requests

response = requests.get("https://api.github.com/salah")
print(response.status_code)