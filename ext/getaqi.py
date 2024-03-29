#เดี๋ยวมาแก้ทีหลัง 10/5/62

import requests

def getRaw(stations):
	#Raw data
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]

def getPM25(stations):
	#PM2.5 value
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['PM25']['value']

def getPM10(stations):
	#PM10 value
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['PM10']['value']

def getAQI(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['AQI']['aqi']

def getLastDate(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['date']

def getLastTime(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['time']


def getO3(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['O3']['value']

def getCO(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['CO']['value']

def getNO2(stations):	
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['NO2']['value']

def getSO2(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['SO2']['value']
