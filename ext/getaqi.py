import requests

def getRaw(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]

def getPM25(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['PM25']['value']

def getPM10(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['PM10']['value']

def getPM25(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]['AQILast']['AQI']['aqi']
