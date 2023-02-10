import requests
response = requests.delete('http://127.0.0.1:5000/ads/2')
print(response.status_code)
print(response.json())

# response = requests.patch('http://127.0.0.1:5000/ads/3', json={'title': 'dddddddddddd', 'description': 'dddddddd', 'owner': 'ddddd' })
# print(response.status_code)
# print(response.json())
#
response = requests.get('http://127.0.0.1:5000/ads/2')
print(response.status_code)
print(response.json())

# response = requests.post('http://127.0.0.1:5000/ads', json={'title': 'vasy11', 'description': 'glvkskmv8JM!@', 'owner': 'fghgh' })
# print(response.status_code)
# print(response.json())
