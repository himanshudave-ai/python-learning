
import requests

url = "https://example.com"

response = requests.get(url, timeout=10)

print("WEBSITE REQUEST DETAILS")

print("URL:", url)
print("Status Code:", response.status_code)
print("Is Successful:", response.ok)
print("Content Type:", response.headers.get("Content-Type"))

print("\nFirst 300 Characters:")
print(response.text[:300])
