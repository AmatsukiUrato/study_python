# coding: utf-8

import requests
import yaml
from bs4 import BeautifulSoup
import json
import re

if __name__ == "__main__":
    session = requests.Session()

    response = session.get("https://jp.techcrunch.com/")

    soup = BeautifulSoup(response.text, "html.parser")

    print(type(soup.find_all(id="river1")[1].find_all("li")))
    for tag in soup.find_all(id="river1")[1].find_all("li", attrs={"data-sharetitle":re.compile(".*")}):
        print(tag["data-sharetitle"])