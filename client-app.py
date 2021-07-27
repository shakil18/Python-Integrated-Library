import sys
import os

# To add library instead installing on the system
LIBRARY_PATH = os.getcwd()
LIBRARY_NAME = "requests"
sys.path.append(os.path.join(LIBRARY_PATH, LIBRARY_NAME))

import requests as req

resp = req.get("http://www.webcode.me")
print(f"============> {resp.status_code} <============")

resp = req.get("http://www.webcode.me/news")
print(f"============> {resp.status_code} <============")
