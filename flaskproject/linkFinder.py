from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value).strip()
                    if url[-1] == '/':  # to remove trailing backslash '/'
                        url = url[:-1]  # to avoid duplicate hompage links
                    self.links.add(url)
                    # print(url)

    def page_links(self):
        return self.links
# federn.org


# finder = LinkFinder('https://CayorEnterprises.com', 'https://CayorEnterprises.com')
# finder.feed("<html><body></body><p>TESTING<a href='https://CayorEnterprises.com'>Tbjjc</a>"
#             "<a href='/videos'>Tbjjc</a></p><a href='/services'>Tbjjc</a></html>")
