import requests
import time
# this is more like an HTTP request but it is very close to an API request
while True:
    req = requests.get('https://kalob.io')
    print(req.status_code)
    time.sleep(60)
    if req.status_code != 200:
        # Email or text me if the site is down
        pass
