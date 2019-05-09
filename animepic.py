import requests

class genAnimePicture:
    animeTypesList = [
        'neko',
        'futa',
        'kawaii',
        'slave',
        'pat',
        'monster'
    ]
	
    def __init__(self, type):
        if type.lower() not in self.animeTypesList:
            raise ValueError('Type of anime not in anime types list')
        req = requests.get(f"https://api.lolis.life/{type.lower()}")
        self.url = req.json()['url']

    def __repr__(self):
        return None if not hasattr(self, 'url') else self.url

if __name__ == '__main__':
	print(genAnimePicture('neko'))
