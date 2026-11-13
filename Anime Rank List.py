from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_anime_series_listed_among_the_best'

headers = {
    'User-Agent':'Chrome/122.0.0.0'
}

page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table', class_ = 'wikitable sortable')

header_row = table.find('tr')

table_titles = [th.text.strip() for th in header_row.find_all('th')][:4]

df = pd.DataFrame(columns=table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:                      # [1:] skips the header row
    row_data = row.find_all(['th', 'td'])[:4]     # th AND td, first 4 columns only
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data

print(df.head())

df.to_csv(r'D:\Files\Anime_list.csv', index=False, encoding='utf-8-sig')