# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

querystring = {"page": 1}
url = "http://zhushou.360.cn/list/index/cid/1"
for i in range(1, 25):
    querystring["page"] = i
    html_doc = requests.request("GET", url, params=querystring)
    soup = BeautifulSoup(html_doc.content, "lxml")
    a_list = soup.select("#iconList > li > a.dbtn")
    for a in a_list:
        print(a.attrs["href"].split("&url=")[1])
