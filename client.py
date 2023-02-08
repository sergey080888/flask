import requests
# response = requests.delete('http://127.0.0.1:5000/users/1')
# print(response.status_code)
# print(response.json())

# response = requests.get('http://127.0.0.1:5000/users/15')
# print(response.status_code)
# print(response.json())

response = requests.post('http://127.0.0.1:5000/users', json={'username': 'vasy11', 'password': 'glvkskmv8JM!@' })
print(response.status_code)
print(response.json())
