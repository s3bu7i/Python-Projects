
import requests

import bs4

r = requests.get("https://www.robocombo.com/Arduino-UNO-R3-CH340")
soup = bs4.BeautifulSoup(r.content,"html5lib")

fiyat=soup.find('span',attrs={"class":"spanFiyat"}).text
print(fiyat)