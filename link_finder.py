from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):  # base_url is the homepage and page_url is a page inside homepage
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':  # 'a' means in html that its a title
            for (attribute, value) in attrs:
                if attrs == 'href':  # 'href' is the attribute that means its a link
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass

