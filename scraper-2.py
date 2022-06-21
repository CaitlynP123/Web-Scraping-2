from selenium import webdriver
from bs4 import BeautifulSoup as bs

import pandas as pd
import time, csv
import requests

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(url)

soup = bs(page.text, 'html.parser')

dwarfs_table = soup.find_all('table')
rows = dwarfs_table[7].find_all('tr')

temp_list = []
headers = ['Star_names', 'Distance', 'Mass', 'Radius']

for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_Names = []
Distance = []
Mass = []
Radius = []

for i in range(1, len(temp_list)):
    Star_Names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

star_data = pd.DataFrame(list(zip(Star_Names, Distance, Mass, Radius)))
star_data.to_csv('dwarfs.csv', header=headers, index=False)