from general import *
from post_content_finder import *


def write_counts(keyword_list, url, crawled_file):
    write_file(crawled_file,
               f'Found the following words in {crawled_file} (firs post was at dd/mm/yyyy):')
    for keyword_num in range(len(keyword_list)):
        write_file(crawled_file, f'{keyword_list[keyword_num-1]} found: {keyword_i_num_in_headline(url, keyword_list, keyword_num-1)}')


