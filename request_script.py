import requests

response = requests.get("https://art-of-fullstack.net") #add params
print(response.status_code)  # Print the status code of the response
#print(response.json())
