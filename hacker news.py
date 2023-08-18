import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')


soup = BeautifulSoup(response.text,'html.parser')

links = soup.select('.titleline')
votes = soup.select('.score')


def custom_hacker_news(links,votes):
    hn = []

    for idx, item in enumerate(links):

        title = links[idx].getText()
        temp = links[idx].select('a')[0]
        href = temp.get('href',None)

        points = int(votes[idx].getText().replace(' points','')) if idx < len(votes) else 0
        if points >= 100:
            hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'],reverse=True)

pprint.pprint(custom_hacker_news(links, votes))