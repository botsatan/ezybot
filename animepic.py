#https://api.lolis.life

import requests

animePic = [
    'neko',
    'futa',
    'kawaii',
    'slave',
    'pat',
    'monster'
]

def genAnimePic(type):
    if type.lower() in animePic:
        req = requests.get(f"https://api.lolis.life/{type.lower()}")
        return req.json()['url']
    return None
