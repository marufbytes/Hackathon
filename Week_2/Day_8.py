import requests
url = "https://official-joke-api.appspot.com/random_joke"
resporse = requests.get(url)
print(resporse.text)