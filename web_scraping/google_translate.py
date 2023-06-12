import requests

url = "https://translate.google.com/_/TranslateWebserverUi/data/batchexecute"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

data = {

    "f.req": '[[["AVdN8","[\\"test\\",\\"en\\",\\"zh-CN\\"]", null, "generic"]]]',
    "at": "ABklwfbOdt4L-g-I2zBeArgpKUZ7:1686537949265"
}

response = requests.post(url=url, data=data)
print(response.text)
