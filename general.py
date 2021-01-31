import os
import http.client
import urllib
import requests


def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"created project '{directory}'")


def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, '')
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    file = open(path, 'w')  # 'w' stands for 'write'
    file.write(data)
    file.close()


def append_to_file(path, data):
    with open(path, 'a') as file:  # 'a' stands for 'append'
        file.write(data + '/n')


def delete_file_content(path):
    with open(path, 'w'):
        pass


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:  # 'rt' for 'read textfile'
        for line in file:
            results.add(line.replace('/n', ''))
    return results


def set_to_file(links, file):
    delete_file_content(file)  # delete because the newest links are in the set, not the file
    for link in sorted(links):
        append_to_file(file, link)


def get_web_request(url):
    dat = {'q': 'goog'}
    connected_web = requests.get(url, params=dat, headers={'User-Agent': 'Mozilla'})
    return connected_web


def get_subreddit_link():
    connected = False
    while not connected:
        subreddit_to_crawl = input(
            'What Subreddit do you want to crawl (just the name without special characters)? >> ')
        url_user = f'http://www.reddit.com/r/{subreddit_to_crawl}/'
        if get_web_request(url_user).status_code == 200:  # 200 means the request was successful, so the webpage exists
            print(f'Great choice! The Subreddit at {url_user} was found')
            return url_user
        else:
            print('Please choose another subreddit, this one doesn\' exist')
