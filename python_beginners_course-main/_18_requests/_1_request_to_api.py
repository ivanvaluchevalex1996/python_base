import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1', verify=False)
print("🟢🔴 ~ :5 ~ response.json()🟢🔴", response.json())
