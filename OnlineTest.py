

import requests

url = "https://raw.githubusercontent.com/Loukaysi/TestOnline/refs/heads/main/TestRead.txt"
response = requests.get(url)

if response.status_code == 200:
    content = response.text
    print(content)
else:
    print(f"Failed to fetch file: {response.status_code}")