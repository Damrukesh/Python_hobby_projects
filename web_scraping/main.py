from bs4 import BeautifulSoup
import requests

web=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webt=web.text
soup=BeautifulSoup(webt,"html.parser")  
movielist=[g.getText() for g in soup.find_all(name="h3",class_="title")]
for d in range(len(movielist)):
    print(movielist[len(movielist)-d-1])
    

# sel=soup.find_all(name="p")

    
# sel=soup.find(name="h1",id="name")    
# print(sel.get_text())