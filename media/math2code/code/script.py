import requests


url = 'https://datacrystals.net/cs/applabsite/CSP_Projects-master/image_net/index.html'

r = requests.get(url)
with open('index.html', 'w') as f:
	f.write(r.text)