
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://quotes.toscrape.com/"

response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("WEBSITE LINKS")

links = soup.find_all("a")

for link in links:
    href = link.get("href")

    if href:
        full_url = urljoin(url, href)
        link_text = link.get_text(strip=True)

        print("Text:", link_text)
        print("URL:", full_url)
        print("-" * 40)
