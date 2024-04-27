import requests

res = requests.get("http://127.0.0.1:8000/items?skip=0&limit=2")

print("Text: ",res.text)
print("Json: ",res.json())
print("Status code: ",res.status_code)