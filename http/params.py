import requests

url = 'https://icanhazdadjoke.com/search'

res = requests.get(
    url,
    headers={'Accept':'application/json'},
    params={'term': 'fruit','limit':1}
    )

data = res.json()
result = data['results']
joke = result[0]['joke']
print(joke)
