import json
from urllib.request import urlopen

url = "https://jsonplaceholder.typicode.com/posts"

with urlopen(url) as response:
    posts = json.loads(response.read().decode("utf-8"))

print("FILTERING API DATA")
print("------------------")

# Filter posts created by user 1
filtered_posts = []

for post in posts:
    if post["userId"] == 1:
        filtered_posts.append(post)

print("Total Posts by User 1:", len(filtered_posts))

print("\nFIRST 5 FILTERED POSTS")

for post in filtered_posts[:5]:
    print("Post ID:", post["id"])
    print("Title:", post["title"])
    print("----------------------")