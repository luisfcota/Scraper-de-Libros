import requests 
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

books_data = []

for page in range(1, 51):
    
    url = base_url.format(page)

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, "html.parser")
    
        book_containers = soup.find_all("article", class_="product_pod")
    
        for book in book_containers:
        
            title = book.h3.a["title"]
        
            price = book.find("p", class_="price_color").text

            books_data.append({"titulo": title, "precio": price})

    else:
        print("El Scraper no funcionó.")
    
df = pd.DataFrame(books_data)

df.to_csv("books.csv", index=False)

print("Datos guardados de manera exitosa en books.csv")


