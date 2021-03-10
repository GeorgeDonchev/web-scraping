import requests
import pandas as pd
from bs4 import BeautifulSoup


def url_to_file(url, file ='file_name.html'):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        with open(file , 'w') as fl:
            fl.write(html_text)
        return html_text
    return ''


year = int(input())
url = f'https://www.boxofficemojo.com/year/world/{year}/'
soup = BeautifulSoup(url_to_file(url), 'html.parser')
table_list =[]
rows = soup.find_all('tr')
headers = [r.text.strip() for r in rows[0]]

for row in rows[1:]:
    current_row = []
    for cell in row:
        current_row.append(cell.text.strip())
    table_list.append(current_row)

db = pd.DataFrame(table_list, columns = headers)
db.to_csv(f'movies-{year}.csv', index = False)