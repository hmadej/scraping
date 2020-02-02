import datetime
import random

from scrap import get_links_wiki


def main():
    pages = get_links_wiki('/wiki/Kevin_Bacon')
    visited = set()
    random.seed(datetime.datetime.now())
    while len(pages) > 0:
        page = pages[random.randint(0, len(pages) - 1)]
        link = page['href']
        if link not in visited:
            visited.add(link)
            pages = get_links_wiki(link)
            print(link)
        else:
            pages.remove(page)


if __name__ == '__main__':
    main()
