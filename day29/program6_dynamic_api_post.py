import json
from urllib.request import Request, urlopen

url = "https://jsonplaceholder.typicode.com/posts"

title = input("Enter post title: ")
body = input("Enter post description: ")

post_data = {
    "title": title,
    "body": body,
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

print("\nPOST REQUEST SUCCESSFUL")
print("----------------------")
print("ID:", result["id"])
print("Title:", result["title"])
print("Body:", result["body"])