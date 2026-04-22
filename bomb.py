import requests

webhook-url = "insert url here"
message-data = {
  "content": "insert any text you want",
  "username": "insert username"
}

print("bombing has begun")
while True:
  response = requests.post(webhook-url, json=data)
