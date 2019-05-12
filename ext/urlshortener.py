import requests

def urlshort(url):
	api = "https://pasunx.tk/api/urlshorten.php"
	if url.startswith("http://"):
		short = requests.post(api, params={"url":url})
		return short.json()['text']
		#return short.json()
	else:
	    return 'ERR'
		
	if url.startswith("https://"):
		short = requests.post(api, params={"url":url})
		return short.json()['text']
		#return short.json()
	else:
	    return 'ERR'
