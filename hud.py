#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


url = "http://192.168.1.11/"

localtx = "http://192.168.1.11/mmdvmhost/localtx.php"

data = requests.get(url)

print(data.content, "html.parser")




