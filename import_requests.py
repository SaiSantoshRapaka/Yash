import requests
import bs4
import lxml

url = requests.get("https://en.wikipedia.org/wiki/Adipurush")
#url = url.text
#print(url.text)

htmldata = bs4.BeautifulSoup(url.text,"lxml")
print(htmldata)
