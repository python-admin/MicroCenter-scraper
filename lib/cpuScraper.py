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
        ghz = name.find("GHz")
        frequency = float(name[ghz - 3:ghz])
        price = data["data-price"]
        csvWriter.writerow([name, brand, socket, frequency, price])
def start():
    link = 'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966995+4294820689+4294819840&myStore=false&rpp=96'
    csvFile = open("cpu.csv", mode = "w")
    fields = ["name", "brand", "socket", "frequency", "price"]
    csvWriter = csv.writer(csvFile, dialect = "excel")
    csvWriter.writerow(fields)
    productList = scrape(link)
    parse(productList, csvWriter)
    csvFile.close()
start()