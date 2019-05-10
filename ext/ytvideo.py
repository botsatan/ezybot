import requests, json
import urllib.request
from bs4 import BeautifulSoup

class youtubeSearch:
    def __init__(self, query):
        if not isinstance(query, str):
            raise ValueError('Query must be strings')
        if query.replace(' ','') != '':
            self.result = []
            searchURL = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
            response = urllib.request.urlopen(searchURL)
            soup = BeautifulSoup(response.read(), 'html.parser')
            for video in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                self.result.append({'title': video['title'], 'url': f"https://youtube.com{video['href']}"})

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, ', '.join(['%s=%r' % (key, value) for key, value in self.__dict__.items()]))
    
if __name__ == '__main__':
    print(youtubeSearch('ยอม legendboy'))
