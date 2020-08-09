import requests
from bs4 import BeautifulSoup
def findMatch(name, arr):
    for e in arr:
        if e in name:
            return e
def scrape(link):
    page = requests.get(link)
    data = page.text
    soup = BeautifulSoup(data, features="lxml")
    productList = (((((soup.find("body")).find("main")).find("article")).find("div", id = "contentResults")).find("article", id = "productGrid")).find("ul", role = "tabpanel")
    return productList.find_all("li", class_ = "product_wrapper")
