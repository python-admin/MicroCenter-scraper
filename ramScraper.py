from bs4 import BeautifulSoup
import csv
from mainLib import findMatch, scrape
def parse(productList, csvWriter):
    for product in productList:
        data = (product.find("div", class_ = "result_left")).find("a", class_ = "image")
        name = data["data-name"]
        brand = data["data-brand"]
        ramTypes = ["DDR2", "DDR3", "DDR4"]
        ramType = findMatch(name, ramTypes)
        channels = ["Single", "Dual", "Quad"]
        channel = findMatch(name, channels)
        name_list = name.split(' ') 
        for word in name_list:
            if 'GB' in word:
                capacity = word[:-2]
                if capacity is not 'R':
                    capacity = int(capacity)
                    break
        ecc = "ECC" in name
        rgb = "RGB" in name
        price = data["data-price"]
        csvWriter.writerow([name, brand, ramType, channel, capacity, ecc, rgb, price])
def start():
    link1 = 'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966965&myStore=false&rpp=96'
    link2 = 'https://www.microcenter.com/search/search_results.aspx?N=4294966965&NTK=all&page=2&cat=Desktop-Memory/RAM-:-MicroCenter'
    csvFile = open("ram.csv", "w")
    csvWriter = csv.writer(csvFile, dialect = "excel")
    fields = ["name", "brand", "type", "channel", "capacity", "ECC", "RGB", "price"]
    csvWriter.writerow(fields)
    productList = scrape(link1)+ scrape(link2)
    parse(productList, csvWriter)
    csvFile.close()
start()