import sys

# To add library instead installing on the system
LIBRARY_PATH = "/home/client-app/repo"
sys.path.append(LIBRARY_PATH)

import requests as req

resp = req.get("http://www.webcode.me")
print(f"============> HTTP Response messeage for 'http://www.webcode.me': {resp.status_code} <============")

resp = req.get("http://www.webcode.me/news")
print(f"============> HTTP Response messeage for 'http://www.webcode.me/news': {resp.status_code} <============")
