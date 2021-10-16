from bs4 import BeautifulSoup
import requests
f = open("noun+es.txt", "w")
url = 'https://en.wiktionary.org/w/index.php?title=Category:English_plurals_ending_in_%22-es%22&pagefrom=arcubuses#mw-pages'

i = 0 
# while url != 'https://en.wiktionary.org/w/index.php?title=Category:English_adjectives&subcatfrom=zz&filefrom=zz&pagefrom=zz#mw-pages':
while url != 'https://en.wiktionary.org/w/index.php?title=Category:English_plurals_ending_in_%22-es%22&pagefrom=white+beeches#mw-pages':

    # try:
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    divclass = soup.select(".mw-category")
    if len(divclass)>1:
        lis = divclass[1].contents
    else:
        lis = divclass[0].contents
    # divlink = soup.select("#mw-pages")
    # print((divlink[0].contents)[5])

    for div in lis:
        li = div.contents[2].contents
        for z in range(0, len(li), 2):
            f.write(li[z].contents[0].contents[0] + "\n")

    

    link = soup.select("#mw-pages")[0].contents[7]
    url = 'https://en.wiktionary.org' + str(link['href'])
    # except:
    #     break
    # print(str(link['href']))
    i = i+1
    print(i)

f.close()