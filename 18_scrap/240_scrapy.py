import pprint
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
#print(res.headers['Set-Cookie'].strip('domain'))
#print(dir(res))
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sorted_data_byvotes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)

def custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            
            if points > 99:
                hn.append({'title': title, 'href':href, 'votes': points})



        # My decision is --> 
        # points = int(votes[idx].getText().replace(' points', ''))
        # if points >= 100:
        #     title = links[idx].getText()
        #     href = links[idx].get('href', None)
            
        #     hn.append({'title': title, 'href':href, 'votes':points}) 
    return sorted_data_byvotes(hn)

pprint.pprint(custom_hn(links, subtext))

