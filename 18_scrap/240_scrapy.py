import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
#print(res.headers['Set-Cookie'].strip('domain'))
#print(dir(res))
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')

def custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        points = int(votes[idx].getText().replace(' points', ''))
        if points >= 100:
            title = links[idx].getText()
            href = links[idx].get('href', None)
            
            hn.append({'title': title, 'href':href, 'votes':points}) 
    return hn

print(custom_hn(links, votes))

