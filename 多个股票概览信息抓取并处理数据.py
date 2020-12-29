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


stock_list = ["AAPL","BABA"]

for stock in stock_list:
    response = requests.get(url_summary.format(stock,stock))
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')
    table = soup.find_all("table" ,{"class" : "W(100%) M(0) Bdcl(c)"})
    stock_summary = []
    for t in table:
        rows = t.find_all ('td')
        for row in rows:
            stock_summary.append(row.get_text())
    stock_summary = np.array(stock_summary)

    name = stock_summary[::2]
    num = stock_summary[1::2]
    print(pd.Series(num,index=name))



















#pattern = re.compile(r'\s--\sData\s--\s')
#script_data = soup.find('script', text = pattern).contents[0]
#print(script_data)
