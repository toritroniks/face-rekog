import requests
ids = [
    '1',
    '2'
]

for id in ids:
    f = open(id + '.jpg','wb')
    f.write(requests.get('http://some-dummy-site.com/' + id + '.jpg').content)
    f.close()
