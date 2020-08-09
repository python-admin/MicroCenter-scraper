from bs4 import BeautifulSoup
import requests
import csv
from mainLib import findMatch, scrape
def parse(productList, csvWriter):
    for product in productList:
        data = (product.find("div", class_ = "result_left")).find("a", class_ = "image")
        name = data["data-name"]
        brand = data["data-brand"]
        memTypes = ["DDR3", "GDDR5X", "GDDR5", "GDDR6", "HBM2"]
        memType = findMatch(name, memTypes)
        name_list = name.split(' ')
        for word in name_list:
            if 'GB' in word:
                memSize = word[:-2]
                if memSize is not 'R':
                    memSize = int(memSize)
                    break
        price = data["data-price"]
        csvWriter.writerow([name, brand, memType, memSize, price])
def start():
    link1 = 'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966937&myStore=false&rpp=96'
    link2 = 'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966937&myStore=false&rpp=96&page=2'
    csvFile = open("gpu.csv", "w")
    csvWriter = csv.writer(csvFile, dialect = "excel")
    fields = ['name', 'brand', 'chipset', 'MemoryType', 'MemorySize', 'price']
    csvWriter.writerow(fields)
    productList = scrape(link1) + scrape(link2)
    parse(productList, csvWriter)
    csvFile.close()
start()