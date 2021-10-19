f = open("./noun_y_or_ey=>ies.txt","r")
from bs4 import BeautifulSoup
import requests

string =f.read().splitlines()
for word in string:
    sub_url="https://en.wiktionary.org/wiki/" + word + "#English"

# sub_url = 'https://en.wiktionary.org' + str(li[z].contents[0]['href'])
    r_sub = requests.get(sub_url)
    doc = r_sub.text
    sub_soup = BeautifulSoup(doc, 'html.parser')
    page = sub_soup.select(".mw-parser-output")[0].ol.i.a.contents[0]
    print(page)