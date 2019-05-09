#https://api.lolis.life

import requests

def genNeko():
    req = requests.get("https://api.lolis.life/neko")
    return req.json()['url']

def genFuta():
    req = requests.get("https://api.lolis.life/futa")
    return req.json()['url']

def genKawaii():
    req = requests.get("https://api.lolis.life/kawaii")
    return req.json()['url']

def genLewd():
    req = requests.get("https://api.lolis.life/lewd")
    return req.json()['url']

def genSlave():
    req = requests.get("https://api.lolis.life/slave")
    return req.json()['url']

def genPat():
    req = requests.get("https://api.lolis.life/pat")
    return req.json()['url']

def genMonster():
    req = requests.get("https://api.lolis.life/monster")
    return req.json()['url']
