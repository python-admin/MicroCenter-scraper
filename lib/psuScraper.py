from bs4 import BeautifulSoup
import csv
from mainLib import findMatch, scrape
def parse(productList, csvWriter):
    for product in productList:
        data = (product.find("div", class_ = "result_left")).find("a", class_ = "image")
        name = data["data-name"]
        brand = data["data-brand"]
        name_list = name.split(' ')
        if "Watt" in name_list:
            if "Watt" in name_list:
                wattage = name_list[name_list.index("Watt") - 1]
            elif "Watts" in name_list:
                wattage = name_list[name_list.index("Watts") - 1]
            if wattage[-1] == "W":
                wattage = int(wattage[:-1])
            else:
                wattage = int(wattage)
        else:
            for word in name_list:
                if word[-1] == "W":
                    wattage = int(word[:-1])
                    break
        rgb = "RGB" in name
        modularity = ["Fully Modular", "Non-Modular", "Semi-Modular"]
        modular = findMatch(name, modularity)
        price = data["data-price"]
        csvWriter.writerow([name, brand, wattage, rgb, modular, price])
def start():
    link = 'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966654&myStore=false&rpp=96'
    csvFile = open("psu.csv", "w")
    csvWriter = csv.writer(csvFile, dialect = "excel")
    fields = ['name', 'brand', 'wattage', 'RGB', 'modular', 'price']
    csvWriter.writerow(fields)
    productList = scrape(link)
    parse(productList, csvWriter)
    csvFile.close()
start()