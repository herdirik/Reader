#web sitesinden veri çekme
from bs4 import BeautifulSoup
import urllib.request
user_agent = ' Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
url = 'https://onedio.com/'
headers = {'User-Agent': user_agent}
request = urllib.request.Request(url, headers=headers)
response= urllib.request.urlopen(request)
soup = BeautifulSoup(response, 'html.parser')# BeautifulSoup yolladık.
liste=soup.find_all('article',limit=10)
print(liste[0].text)
f=open("onedio.txt","w")
for i in range(0,9):
   f.write(liste[i].text)
   f.write("\n")