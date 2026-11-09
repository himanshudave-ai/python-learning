import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

url = "https://jsonplaceholder.typicode.com/invalid-endpoint"

try:
    with urlopen(url, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
        print("Data fetched successfully!")
        print(data)

except HTTPError as error:
    print("HTTP Error:", error.code)

except URLError as error:
    print("Connection Error:", error.reason)

except TimeoutError:
    print("Request timed out!")

except json.JSONDecodeError:
    print("Invalid JSON response!")