import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
from post_content_finder import *
from word_counter import *


PROJECT_NAME = 'Reddit_Extractor'
HOMEPAGE = 'http://www.reddit.com/r/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 12
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        threads = threading.Thread(target=work)
        threads.daemon = True
        threads.start()


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# each line in the file is a job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# if there are any items in the queue, crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


subreddit_link = get_subreddit_link()
print(subreddit_link)
keyword_list = []
keywords = input('Chose keywords that you want to search for (separate with ", ")? >> ')
if ', ' in keywords:
    keyword_list = keywords.split(', ')  # first keyword ist first item, second the second etc.
elif ',' in keywords:
    keyword_list = keywords.split(',')  # if the user doesn't make a whitespace
else:
    keyword_list.append(keywords)

write_counts(keyword_list, subreddit_link, CRAWLED_FILE)

# create_workers()
# crawl()
