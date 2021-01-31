from urllib.parse import urlparse


def get_domain_name(url):  # eg. (only) example.com
    try:
         results = get_sub_domain_name(url).split('.')
         if 'co' in results:
            return results[-3] + '.' + results[-2] + results[-1]
         else:
            return results[-2] + '.' + results[-1]
    except:
        return ''


def get_sub_domain_name(url):  # eg. name.gv.example.com
    try:
        return urlparse(url).netloc
    except:
        return ''
