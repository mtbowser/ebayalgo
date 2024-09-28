import requests

# eBay Browse API endpoint
url = "https://api.ebay.com/buy/browse/v1/item_summary/search"

# OAuth access token
access_token = "YOUR_ACCESS_TOKEN"

# Define headers with the OAuth token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Define query parameters to search for designer items
designer = "Gucci"  # You can iterate over the designer names list
params = {
    "q": designer,
    "filter": "price:[..100]",  # Find items under $100
    "limit": "10"  # Limit to 10 results
}

# Send request to eBay Browse API
response = requests.get(url, headers=headers, params=params)

# Print the response
print(response.json())

