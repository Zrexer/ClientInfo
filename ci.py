import requests 
import bs4 

respone = requests.get("https://www.askapache.com/online-tools/http-headers-tool/")

soup = bs4.BeautifulSoup(respone.text, "html.parser")

name = []
x = {}
val = []

for i in soup.find_all("input"):
    d = str(i).split("<input")
    for x2 in d:
        x3 = str(x2).split()
        
        for b in x3:
            if b.startswith("name"):
                namex = b.replace("name=", "")
                name.append(namex)
            
            if b.startswith("value"):
                vx = b.replace("value=", "")
                val.append(vx)

for h in range(len(name)):
    c = str(val[h]).replace("/>", "").replace(">", "")
    print(f"Name: {name[h]} => {c}")
