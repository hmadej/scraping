from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_html(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
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


print(get_header(get_html('http://www.pythonscraping.com/pages/page1.html')))
