
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("HTML PARSING")

print("\nPage Title:")
print(soup.title.get_text(strip=True))

print("\nMain Heading:")
heading = soup.find("h1")
print(heading.get_text(strip=True) if heading else "Not found")

print("\nFirst Five Quotes:")
quotes = soup.find_all("span", class_="text")

for quote in quotes[:5]:
    print(quote.get_text(strip=True))
