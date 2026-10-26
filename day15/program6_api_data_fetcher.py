import json
import requests
from pathlib import Path

API_URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_FILE = Path(__file__).with_name("fetched_posts.json")


def fetch_posts():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        posts = response.json()

        if not isinstance(posts, list):
            print("Unexpected API response format.")
            return

        selected_posts = []

        for post in posts[:5]:
            selected_posts.append({
                "id": post["id"],
                "user_id": post["userId"],
                "title": post["title"]
            })

        with OUTPUT_FILE.open("w", encoding="utf-8") as file:
            json.dump(selected_posts, file, indent=4)

        print("Data fetched and saved successfully.")
        print("Number of posts:", len(selected_posts))
        print("Saved file:", OUTPUT_FILE.name)

        for post in selected_posts:
            print("\nPost ID:", post["id"])
            print("User ID:", post["user_id"])
            print("Title:", post["title"])

    except requests.exceptions.Timeout:
        print("Error: API request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Please check your internet connection.")

    except requests.exceptions.HTTPError as error:
        print("HTTP Error:", error)

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

    except (ValueError, KeyError, TypeError) as error:
        print("Invalid API data:", error)

    except OSError as error:
        print("File error:", error)


if __name__ == "__main__":
    fetch_posts()