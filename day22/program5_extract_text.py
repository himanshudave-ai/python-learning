
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("QUOTES AND AUTHORS")

quotes = soup.find_all("div", class_="quote")

for item in quotes:
    quote_text = item.find("span", class_="text")
    author = item.find("small", class_="author")
    tags = item.find_all("a", class_="tag")

    print("\nQuote:", quote_text.get_text(strip=True))
    print("Author:", author.get_text(strip=True))

    print("Tags:", ", ".join(
        tag.get_text(strip=True) for tag in tags
    ))
    print("-" * 50)
