import requests


api_url = "http://shibe.online/api/shibes?count=1"

param = {"count": 10}
response = requests.get(api_url, params=param)


status_code = response.status_code

print(f"Status code is: {status_code}")

response_json = response.json()

print(response_json)
