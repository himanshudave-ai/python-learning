import json
from urllib.request import Request, urlopen

url = "https://jsonplaceholder.typicode.com/posts"

post_data = {
    "title": "Python Automation Project",
    "body": "Learning API integration and automation",
    "userId": 1
}

data = json.dumps(post_data).encode("utf-8")

request = Request(
    url,
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))

print("POST REQUEST SUCCESSFUL")
print("------------------------")
print("Generated Post ID:", result["id"])
print("Title:", result["title"])
print("User ID:", result["userId"])