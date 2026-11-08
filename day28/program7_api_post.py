import json
from urllib.request import Request, urlopen

url = "https://jsonplaceholder.typicode.com/posts"

employee = {
    "title": "Python Learning",
    "body": "Learning JSON and API integration",
    "userId": 1
}

data = json.dumps(employee).encode("utf-8")

request = Request(
    url,
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))

print("API Response Received")
print("---------------------")
print("ID:", result["id"])
print("Title:", result["title"])
print("User ID:", result["userId"])