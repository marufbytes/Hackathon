import requests

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

# Convert response to JSON (dictionary)
data = response.json()

print("FULL JSON:")
print(data)

print("Setup:", data["setup"])
print("Punchline:", data["punchline"])
