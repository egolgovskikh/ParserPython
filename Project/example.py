from urllib3 import request
from bs4 import BeautifulSoup
import urllib3
import urlopen

def get_html(url):
    response = urllib3.request.urlopen(url)
    return response.read()

def main():
    print(get_html("https://www.myscore.ru/football/spain/laliga/fixtures/"))
    print(12)
main()