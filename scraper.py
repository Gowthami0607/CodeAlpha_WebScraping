import requests
from bs4 import BeautifulSoup
import pandas as pd

all_books = []

for page in range(1, 51):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        rating = book.p["class"][1]

        all_books.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })

df = pd.DataFrame(all_books)

df.to_csv(
    "books_dataset.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Total Books Scraped:", len(df))
print("Dataset Saved Successfully!")