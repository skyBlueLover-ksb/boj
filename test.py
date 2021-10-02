"""
import requests

target = "http://google.com"
response = requests.get(url=target)
print(response.text)
"""
"""
import json

user = {
    "id": "gildong",
    "password": "192837",
    "age": 30,
    "hobby": ["football", "programming"],
}

json_data = json.dumps(user)

data = json.loads(json_data)
print(data)
"""
import numpy as np

print([3, 3, 3] / np.float_(3))
