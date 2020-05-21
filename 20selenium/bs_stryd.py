from bs4 import BeautifulSoup


from strydlogin import username, password

import requests

url = 'https://www.stryd.com/powercenterbeta/runs/5782253728366592'

r = requests.get(url, auth=(username, password))

# oup = BeautifulSoup(url, 'html.parser')

print(r.json())