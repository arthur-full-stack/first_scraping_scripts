from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
# Set up the Chrome WebDriver
webdriver_service = Service('/usr/bin/')  # Replace with the path to your chromedriver executable
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Navigate to the webpage
url = "https://art-of-fullstack.net"
driver.get(url)

# Wait for the JavaScript content to load
wait = WebDriverWait(driver, 10)
body_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Get the text from the <body> tag
body_text = body_element.text

# Print the scraped data
print("Scraped Data:")
print(body_text)

# Get the page source
page_source = driver.page_source

image_elements = driver.find_elements("tag name", "img")
#text_elements = driver.find_elements("tag_name", "p")
for index, image_element in enumerate(image_elements):
    image_url = image_element.get_attribute("src")
    image_filename = f"image_{index}.jpg"  # Assign a unique filename for each image
    urllib.request.urlretrieve(image_url, image_filename)
    print(f"Downloaded image: {image_filename}")

# Print the scraped data
print("Scraped Text:")

# Quit the WebDriver
driver.quit()







