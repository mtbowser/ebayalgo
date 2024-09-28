import requests
from bs4 import BeautifulSoup

# SSENSE brands page URL (example URL, check for actual brand listing pages)
url = "https://www.ssense.com/en-us/men/designers" 

# Send a GET request to the page
headers = {"User-Agent": "Mozilla/5.0"}  # Pretend to be a browser
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the elements that contain brand/designer names
# This part might change based on how the website is structured
brands = soup.find_all("a", class_="designer-name")  # Example: class names may vary

# Print the brands or save them to a list
brand_names = []
for brand in brands:
    brand_name = brand.get_text(strip=True)
    brand_names.append(brand_name)
    print(brand_name)
