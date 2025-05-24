from bs4 import BeautifulSoup
import requests

with open("web scraping/website.html") as filee:
    contents=filee.read()
    
soup=BeautifulSoup(contents,"html.parser")    
#print(soup.p )

sel=soup.find_all(name="p")

    
sel=soup.find(name="h1",id="name")    
print(sel.get_text())