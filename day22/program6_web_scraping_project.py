
import requests
import csv
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    data = []

    for item in quotes:
        quote = item.find("span", class_="text")
        author = item.find("small", class_="author")
        tags = item.find_all("a", class_="tag")

        data.append({
            "Quote": quote.get_text(strip=True),
            "Author": author.get_text(strip=True),
            "Tags": ", ".join(
                tag.get_text(strip=True) for tag in tags
            )
        })

    with open("scraped_quotes.csv", "w",
              newline="", encoding="utf-8") as file:

        fieldnames = ["Quote", "Author", "Tags"]

        writer = csv.DictWriter(
            file, fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(data)

    print("SCRAPING COMPLETED SUCCESSFULLY")
    print("Total Quotes Extracted:", len(data))
    print("Data saved in scraped_quotes.csv")

except requests.exceptions.RequestException as error:
    print("Website request error:", error)
