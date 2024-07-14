import requests

# Get the data from the API
response = requests.get('https://jsonplaceholder.typicode.com/users')
json = response.json()
print(json)

for user in json:
    print(user['name'], user['email'])