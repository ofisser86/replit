import pprint
import requests
from bs4 import BeautifulSoup

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

 
pprint.pprint(links_accum(url, count_of_pages))
