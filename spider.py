from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:

    # class variables to share them among all instances
    project_name = ''
    base_url = ''
    domain_name = ''
    queued_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_url):
        self.project_name = project_name
        print(f'heere: {project_name}')
        self.base_url = base_url
        self.domain_name = domain_url
        Spider.queued_file = self.project_name + '/queue.txt'
        Spider.crawled_file = self.project_name + '/crawled.txt'
        self.boot(self)
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot(self):
        print(f'HERE: {self.project_name}')
        create_project_dir(self.project_name)
        create_data_files(self.project_name, self.base_url)
        Spider.queue = file_to_set(self.queued_file)
        Spider.crawled = file_to_set(self.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(f'{thread_name} now crawling {page_url}...')
            # print(f'In Queue: {str(len(Spider.queue))} | Crawled: {str(len(Spider.crawled))}')
            # Spider.add_links_to_queue(Spider.gather_links(page_url))
            # Spider.queue.remove(page_url)
            # Spider.crawled.add(page_url)
            # Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':  # if the spider finds text in the page
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)

        except:
            print('Error: Can not crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:  # dont add to queue if its already there
                continue
            if url in Spider.crawled:  # dont add to queue if it been crawled already
                continue
            if url in Spider.domain_name:  # dont add to queue if its another website
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queued_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
