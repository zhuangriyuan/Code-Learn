from fp.fp import FreeProxy

proxy = FreeProxy(https=True).get()

print(proxy)

url = "test.com"
headers = {

}
html = requests.get(url=url, headers=headers, proxies={"https": proxy})
# 使用proxy绕过ip封锁
