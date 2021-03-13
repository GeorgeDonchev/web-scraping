from bs4 import BeautifulSoup
import requests
import pandas as pd


def url_to_file(url):
    r = requests.get(url)
    if r.status_code == 200:
        content = r.text
        with open('file.html', 'w') as fl:
            fl.write(content)
        return content
    return ''


def parse_to_csv(url):
    soup = BeautifulSoup(url_to_file (url), 'html.parser')
    containers = soup.findAll('div', {'class':'item-container'})
    headers = ['brand', 'price', 'shipping']
    table=[]
    for container in containers:
        title = container.findNext('a', {'class':'item-title'}).text
        raw_price = container.findNext('li', {'class':'price-current'}).text
        price = raw_price.split(' ')[0]
        shipping = container.findNext('li',{'class':'price-ship'}).text
        table.append([title, price, shipping])
    db = pd.DataFrame(table, columns = headers)
    db.to_csv('video-cards.csv', index = True)
    return


url = 'https://www.newegg.com/p/pl?d=graphic+card'
parse_to_csv(url)
