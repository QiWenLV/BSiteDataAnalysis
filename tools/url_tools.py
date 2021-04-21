import requests
from bs4 import BeautifulSoup
import json


def http2json(url, header):
    response = requests.get(url, header)
    if requests is None:
        print(f"{__name__}: 请求错误")
    return json.loads(response.text)
