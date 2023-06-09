import requests
from bs4 import BeautifulSoup

url = "https://art-of-fullstack.net"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('body').text

    print("Scraped Data:")
    print(data)
else:
    print("Error")

