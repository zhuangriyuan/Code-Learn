import requests


url = "https://www.google.com/search?q=hello"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
print(resp.text)
