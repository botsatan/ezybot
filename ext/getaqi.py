import requests

def getAQI(stations):
	req = requests.get("http://air4thai.net/forappV2/getAQI_JSON.php")
	return req.json()['stations'][stations]
