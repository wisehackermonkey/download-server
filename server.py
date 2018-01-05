# import requests

# download_url = "http://127.0.0.1"
# # download_url = 'http://httpbin.org/post'


import requests, time
r = requests.post('https://requestb.in/12ix9ko1', data={"ts":time.time()})
print r.status_code
print r.content