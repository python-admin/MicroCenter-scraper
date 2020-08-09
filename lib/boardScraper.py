from bs4 import BeautifulSoup
import requests
import csv
from mainLib import findMatch, scrape
def parse(productList, csvWriter):
    for product in productList:
        data = (product.find("div", class_ = "result_left")).find("a", class_ = "image")
        name = data["data-name"]
        brand = data["data-brand"]
        sockets = ["AM4", "sTRX4", "LGA 1151", "LGA 1200", "LGA 2066"]
        socket = findMatch(name, sockets)
        formFactors = ["eATX", "mATX", "ATX", "mini DTX", "Mini-DTX", "mini-ITX", "Mini-ITX", "mini ITX", "mITX"]
        formFactor = findMatch(name, formFactors)
        sameForms = {"Mini-DTX": ["mini DTX", "Mini-DTX"], "mini-ITX": ["mini-ITX", "Mini-ITX", "mini ITX", "mITX"]}
        for form in sameForms:
            if formFactor in sameForms[form]:
                formFactor = form
        wifi = 'WiFi' in name or 'WIFI' in name
        price = data["data-price"]
        csvWriter.writerow([name, brand, socket, formFactor, wifi, price])
def start():
    link1 = 'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966996+4294818892+4294818573&myStore=false&rpp=96'
    link2 = 'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966996+4294818892+4294818573&myStore=false&rpp=96&page=2'
    csvFile = open("board.csv", "w")
    csvWriter = csv.writer(csvFile, dialect = "excel")
    fields = ['name', 'brand', 'socket', 'formFactor', 'wifi', 'price']
    csvWriter.writerow(fields)
    productList = scrape(link1) + scrape(link2)
    parse(productList, csvWriter)
    csvFile.close()
start()