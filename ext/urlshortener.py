import requests

def urlshort(url):
	api = "https://pasunx.tk/api/urlshorten.php"
	if url.startswith("http://" or "https://"):
		short = requests.post(api, params={"url":url})
		return short.json()['url']
		#return short.json()
	else:
		return 'ERR'
