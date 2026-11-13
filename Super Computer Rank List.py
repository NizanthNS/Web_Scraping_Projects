from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/TOP500"
headers = {'User-Agent': 'Chrome/122.0.0.0'}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

tables = soup.find_all('table', class_='wikitable sortable')

table = tables[1]

header_row = table.find('tr')
table_titles = [th.text.strip() for th in header_row.find_all('th')]

rows = []
for tr in table.find_all('tr')[1:]:
    cells = [td.text.strip() for td in tr.find_all(['td', 'th'])]
    if cells:
        rows.append(cells)

df = pd.DataFrame(rows, columns=table_titles)
print(df.head())

df.to_csv(r'D:\Files\Super Computer Rank List.csv', index=False, encoding='utf-8-sig')