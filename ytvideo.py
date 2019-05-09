import requests, json
import urllib.request
from bs4 import BeautifulSoup

def ytSearch(song):
    if song == None:
        return "ชื่อวิดีโอไม่สามารถเว้นว่างได้"
    if song != None:
        ssong = str(song)
        query = urllib.parse.quote(ssong)
        yturl = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(yturl)
        ht = response.read()
        soup = BeautifulSoup(ht, 'html.parser')
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            req = requests.get("https://pasunx.tk/api/urlshorten.php?url=" + "https://www.youtube.com/watch?v=" + vid['href'])
            return(req.json()['text'])
