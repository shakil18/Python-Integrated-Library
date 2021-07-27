import sys
import os

# To add library instead installing on the system
LIBRARY_PATH = os.getcwd()
LIBRARY_NAME = "requests"
sys.path.append(os.path.join(LIBRARY_PATH, LIBRARY_NAME))

import requests as req

print(f"============> Using 3rd party Library: '{LIBRARY_NAME}' <============")

resp = req.get("http://www.webcode.me")
print(f"============> HTTP Response messeage for 'http://www.webcode.me': {resp.status_code} <============")

resp = req.get("http://www.webcode.me/news")
print(f"============> HTTP Response messeage for 'http://www.webcode.me/news': {resp.status_code} <============")
