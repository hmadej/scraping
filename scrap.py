import re
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_html(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as _:
        print("server could not be found")
    else:
        return html
    return None


def get_header(html):
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.h1
    except AttributeError as e:
        print(e)
        return None
    return title


def get_links_wiki(article):
    bs = BeautifulSoup(get_html('http://en.wikipedia.org{}'.format(article)), 'html.parser')
    links = []
    pattern = re.compile('^(/wiki/)((?!:).)*$')
    try:
        for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=pattern):
            if 'href' in link.attrs:
                links.append(link)
    except AttributeError as e:
        print(e)

    return links


def main():
    html = get_html('http://www.pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html.read(), 'html.parser')
    name_list = bs.find('table', {'id': 'giftList'}).tr.next_siblings
    for sibling in name_list:
        print(sibling)


if __name__ == '__main__':
    main()
