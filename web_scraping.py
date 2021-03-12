from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.newegg.com/p/pl?d=graphic+card'

r = requests.get(url)
content = r.text
with open('file.html', 'w') as fl:
    fl.write(content)
pattern = '("View Details">)([a-zA-Z0-9, -.]+)[<$]'

soup = BeautifulSoup(content, 'html.parser')
containers = soup.findAll('div', {'class':'item-container'})
headers = ['brand', 'price', 'shipping']
table=[]
for container in containers:
    current_data = []
    title = container.findNext('a', {'class':'item-title'}).text
    raw_price = container.findNext('li', {'class':'price-current'}).text
    price = raw_price.split(' ')[0]
    shipping = container.findNext('li',{'class':'price-ship'}).text
    current_data.append(title)
    current_data.append(price)
    current_data.append(shipping)
    table.append(current_data)
db = pd.DataFrame(table, columns = headers)
db.to_csv('video-cards.csv', index = True)