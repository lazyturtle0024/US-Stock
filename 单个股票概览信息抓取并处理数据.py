# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

url_summary = 'https://finance.yahoo.com/quote/{}?p={}'

stock = 'BABA'



response = requests.get(url_summary.format(stock,stock))
page_content = response.content
soup = BeautifulSoup(page_content, 'html.parser')

#tabl = soup.find_all("span" ,{"class" : "Trsdu(0.3s) "})
table = soup.find_all("table" ,{"class" : "W(100%) M(0) Bdcl(c)"})
#print(table)

stock_summary = []

for t in table:
    rows = t.find_all ('td')
    for row in rows:
        #print(row.get_text())
        stock_summary.append(row.get_text())


print(stock_summary)

stock_summary = np.array(stock_summary)

name = stock_summary[::2]
num = stock_summary[1::2]


print(name)
print(num)

print(pd.Series(num,index=name))




















#pattern = re.compile(r'\s--\sData\s--\s')
#script_data = soup.find('script', text = pattern).contents[0]
#print(script_data)
