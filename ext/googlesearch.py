import requests
from bs4 import BeautifulSoup

def googlesearch(search):
    req = requests.get("https://www.google.com/search", params={"q":search} headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
    soup = BeautifulSoup(req.text, 'html.parser')
    f_results = []
    r_block = soup.find_all('div', attrs={'class': 'g'})
    for result in r_block:
        link = result.find('a', href=True)
        title = result.find('h3')
        description = result.find('span', attrs={'class': 'st'})
        if link and title:
            link = link['href']
            title = title.get_text()
            if description:
                description = description.get_text()
            if link != '#':
                f_results.append({'search': search, 'title': title, 'description': description, 'link': link})
    return f_results
