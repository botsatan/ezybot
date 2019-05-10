import requests, urllib
from bs4 import BeautifulSoup

class googleSearch:
    def __init__(self, query):
        if not isinstance(query, str):
            raise ValueError('Query must be strings')
        if query.replace(' ','') != '':
            self.result = []
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0'}
            req = requests.get("https://www.google.com/search", params={"q": query})
            soup = BeautifulSoup(req.text, 'html.parser')
            for result in soup.find_all('div', attrs={'class': 'g'}):
                link = result.find('a', href=True)
                title = result.find('h3')
                description = result.find('span', attrs={'class': 'st'})
                if link and title:
                    if link != '#':
                        self.result.append({'title': title.get_text(), 'description': '' if not description else description.get_text(), 'link': urllib.parse.unquote(link['href'][7:])})
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, ', '.join(['%s=%r' % (key, value) for key, value in self.__dict__.items()]))
    
if __name__ == '__main__':
    print(googleSearch('ยอม legendboy'))
