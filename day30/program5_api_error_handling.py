import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

url = "https://jsonplaceholder.typicode.com/users"

try:
    with urlopen(url, timeout=10) as response:
        users = json.loads(response.read().decode("utf-8"))

    print("API DATA FETCHED SUCCESSFULLY")
    print("Total users:", len(users))

except HTTPError as error:
    print("HTTP Error:", error.code)

except URLError as error:
    print("Connection Error:", error.reason)

except json.JSONDecodeError:
    print("Error: Invalid JSON response")

except TimeoutError:
    print("Error: Request timed out")

print("Program execution completed.")