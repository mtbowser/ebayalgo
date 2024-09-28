import requests

# Define the eBay Browse API endpoint
url = "https://api.ebay.com/buy/browse/v1/item_summary/search"

# OAuth token
access_token = "YOUR_ACCESS_TOKEN"

# Define the headers with the OAuth token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Define the query parameters to find cheap items
params = {
    "q": "laptop",  # Search keyword
    "filter": "price:[..100]",  # Items under $100
    "limit": "10"  # Limit to 10 results
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Print the response
print(response.json())

