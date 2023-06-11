import urllib.request

url = "http://wwww.baidu.com"

response = urllib.request.urlopen(url=url)
print(response)
