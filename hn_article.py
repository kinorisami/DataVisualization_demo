from textwrap import indent

import requests
import json

url="https://hacker-news.firebaseio.com/v0/item/31353677.json"
r= requests.get(url)
print(f"Stuats Code:{r.status_code}")

response_dict =r.json()
resonse_string = json.dumps(response_dict,indent =4)
print(resonse_string)