import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: API returned invalid JSON.")
    else:
        print("API request successful.")
        print("Post ID:", data.get("id"))
        print("Title:", data.get("title"))

except requests.exceptions.Timeout:
    print("Error: Request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Check your internet connection.")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)