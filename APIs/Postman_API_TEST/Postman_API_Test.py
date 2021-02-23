import requests

link = "https://postman-Echo.com/basic-auth"

response = requests.get(link, auth = ("postman", "password"))

print(response)
print(response.text)
