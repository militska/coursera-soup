import requests
from bs4 import BeautifulSoup


def exec():
    for page_number in range(1, 92):
        req = requests.get('https://www.coursera.org/directory/courses?page=' + str(page_number))
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        list_courses = soup.find('div', {"class": "rc-LinksContainer"})
        items = soup.find_all('li', list_courses)

        for item in items:
            print(item)
            print(item.find('a')['href'])
            print("Название курса ")
            print(item.find('a').contents)

            print_base_info(item)


def print_base_info(course):
    req_courses = requests.get('https://www.coursera.org' + course.find('a')['href'])
    html_courses = req_courses.text
    soup_courses = BeautifulSoup(html_courses, 'lxml')
    about = soup_courses.find('div', {"class": "content-inner"})

    print("Описание курса ")
    print(about)


exec()
