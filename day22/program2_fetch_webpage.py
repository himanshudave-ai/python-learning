
import requests

url = "https://example.com"

try:
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    print("WEBPAGE FETCHED SUCCESSFULLY")

    print("\nWebsite URL:", response.url)
    print("Status Code:", response.status_code)
    print("HTML Content Length:", len(response.text))

    print("\nComplete HTML Content:")
    print(response.text)

except requests.exceptions.RequestException as error:
    print("Error occurred:", error)
