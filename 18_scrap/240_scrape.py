import pprint
import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/news'
payload = {'p': 1}
res = requests.get('https://news.ycombinator.com/news', params=payload)
res2 = requests.get('https://news.ycombinator.com/news', params={'p': 2})
#print(res.headers['Set-Cookie'].strip('domain'))
#print(dir(res))
# soup = BeautifulSoup(res.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')
# links = soup.select('.storylink')
# links2 = soup2.select('.storylink')
# subtext = soup.select('.subtext')
# subtext2 = soup2.select('.subtext')
# def link_generator(url, payload):
#     context = dict()
#     res = requests.get(url, params=payload)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     links = soup.select('.storylink')
#     subtext = soup.select('.subtext')
#     context['links'] = links
#     context['subtext'] = subtext
#     return context
url = 'https://news.ycombinator.com/news'
count_of_pages = 2
def links_accum(url, count_of_pages):
    context = {'links': []}
    
    for page in range(count_of_pages + 1):
        payload = {'p': page}
        res = requests.get(url, params=payload)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        context.update({'links':links})
        context['subtext'] = subtext
    return context



# mega_links = links + links2
# mega_subtext = subtext + subtext2

mega_store = links_accum(url, count_of_pages)

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

pprint.pprint(custom_hn(mega_store['links'], mega_store['subtext']))

