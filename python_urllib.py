from urllib import request, parse

cabecalho = {"User-Agent": "",
             "Cookie": ""}

data = {"login": "", "password": ""}
data = parse.urlencode(data).encode()

req = request.Request("", headers=cabecalho, )
resp = request.urlopen(req)
html = resp.read()
print(html)



