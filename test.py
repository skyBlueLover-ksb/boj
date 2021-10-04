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
import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
l1 = [[] for _ in range(n)]
l1[0].append(1)
l1[0].append(1)
for i in range(1, n):
    l1[i].append(1)
    for j in range(1, i + 1):
        l1[i].append(l1[i - 1][j - 1] + l1[i - 1][j])
    l1[i].append(1)
print(l1[n - 1][k] % 10007)
