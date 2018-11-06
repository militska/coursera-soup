import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.coursera.org/directory/courses?page=1')
html = req.text

soup = BeautifulSoup(html, 'lxml')

list_courses = soup.find('div', {"class": "rc-LinksContainer"});

items = soup.find_all('li', list_courses);

for item in items:
    # print(item)
    print(item.find('a')['href'])
    print(item.find('a').contents)
