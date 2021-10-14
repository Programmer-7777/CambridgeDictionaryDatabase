from bs4 import BeautifulSoup
import requests

url = 'https://en.wiktionary.org/w/index.php?title=Category:English_nouns&pageuntil=1950S%0A1950s#mw-pages'
f = open("noun_lemma.txt", "w")
listt = []

i = 0 
while (url != "https://en.wiktionary.org/w/index.php?title=Category:English_nouns&from=zz"):
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    divclass = soup.select(".mw-category")[1]
    lis = divclass.contents
    k = 0
#     print(len(lis))
    for div in lis:
        if i == 0:
            if k == 0:
                k = k+1
                continue
            else:
                li = div.contents[2].contents
                if len(li) > 1:
                    for z in range(0, len(li), 2):
#                         listt.append(li[z])
#                         print(li[z].contents[0].contents[0])
                        listt.append(li[z].contents[0].contents[0])
                else:
#                     listt.append(li[0])
#                     print(li[0].contents[0].contents[0])
                    listt.append(li[0].contents[0].contents[0])
        else:
            li = div.contents[2].contents
            if len(li) > 1:
                for z in range(0, len(li), 2):
                    listt.append(li[z].contents[0].contents[0])
# #                     print()
                else:
                    listt.append(li[0].contents[0].contents[0])
                    


    link = soup.select('a[title="Category:English nouns"]')[1]
    url = 'https://en.wiktionary.org' + str(link['href'])
    
    i = i+1
    print(i)

for word in listt:
    f.write(word + "\n")
f.close()