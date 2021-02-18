from urllib.request import urlopen

import content as content
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from general import *
from html.parser import HTMLParser
from urllib import parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_html(url):
    temp = urllib.request.urlopen(url)
    html = str(temp.read().decode("utf-8"))
    return html


def keyword_i_num_in_headline(url, keyword_list, keyword_num):
    try:
        # I tried to find the keywords with webdriver, simulating a human scrolling the web and pressing ctrl + f at the very bottom. The problem is that if you search for the keywords like this it can't find all the keywords at once, only the one you se at your screen and a few scrolls up and down

        driver = webdriver.Firefox()

        driver.implicitly_wait(45)
        driver.maximize_window()

        driver.get(url)
        for i in range(10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)

        element = driver.find_element(By.TAG_NAME, 'div')
        elements = element.find_elements(By.TAG_NAME, 'p')
        for e in elements:
            print(e.text)
            # it only prints the elements that you see at the screen
        elem = driver.find_elements_by_class_name('div')
        # here I tried to exctract the html from the webdriver but it either throws an error or returns an empty string
        inner_html = elem.get_attribute('innerHTML')
        print(f'Inner HTML: {inner_html}')

        lists = driver.find_elements_by_name(keyword_list[keyword_num])
        print(f'Key: {keyword_list[keyword_num]}, lists: {lists}, lengh: {len(lists)}')

        # here I tried to extract the html directly with urllib, but the articles are mostly not in the html, they are created by a script in the html, so you can only see the current artices when you scroll
        the_url = requests.get(url).text
        print(f'keyword_list: \'{keyword_list}\'')
        temp = urllib.request.urlopen(url)
        HTML = str(temp.read().decode("utf-8"))
        print(f'HTML: {HTML}')
        print(f'nr of occ of \'{keyword_list[keyword_num]}\' in HTML: {HTML.count(keyword_list[keyword_num])}')

        # here I tried to find all the keywords with beautiful soup, but it seems to work not as good as urllib
        soup = BeautifulSoup(HTML, 'html.parser')
        headlines = soup.find_all('h3')
        print(f'headline: {headlines}')
        print(f'nr of occ of \'{keyword_list[keyword_num]}\' in soup: {headlines.count(keyword_list[keyword_num])}')
    except:
        print('Error: the url was unrechable')


def keyword_i_num_in_post(url, keyword_list, keyword_num):
    web_content = get_web_request(url).content['p']
    return web_content.numberOfOccurrences(keyword_list[keyword_num])

    # web_soup = BeautifulSoup(connected_web.content)
    # for word in web_soup.find_all(id='h3'):


# TODO: search for the post's title and text (links in idea.txt)
# soup.find_all(id='link2')


# TODO: extract the date of the first post of the subreddit or how long the subreddit exists


