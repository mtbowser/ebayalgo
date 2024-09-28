from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the web driver (Make sure to install a web driver like ChromeDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the SSENSE brands page
driver.get("https://www.ssense.com/en-us/men/designers")

# Wait for the page to load and find the brand elements
brands = driver.find_elements(By.CLASS_NAME, "designer-name")

# Collect brand names
brand_names = [brand.text for brand in brands]

# Print the list of brand names
print(brand_names)

# Close the browser
driver.quit()
