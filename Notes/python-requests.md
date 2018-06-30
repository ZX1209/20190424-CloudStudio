## 使用代理

proxies={'http':'127.0.0.1:1080','https':'127.0.0.1:1080'}

requests.get('http://www.google.com',proxies=proxies)

// ok