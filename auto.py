import requests
from bs4 import BeautifulSoup
url = 'https://hackernoon.com/'

response = requests.get(url)
#print (response)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_ = 'title-wrapper')
authors = soup.find_all('div', class_ = 'date')
tags = soup.find_all('div', class_ = 'meta')

for info in range(0, len(quotes)):
    print (quotes[info].text)
    print(authors[info].text)
    tags_info = tags[info].find_all('a', class_ = 'Link-k8dxie-0 edxnaq')
    for tag_info in tags_info:
        print(tag_info.text)