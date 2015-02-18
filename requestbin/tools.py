"""
common tools module
"""

def normalize_url(url):
    '''remove stacked forward slashes and trailing slash'''
    import re
    return re.sub('([^:])///*', r'\1/', url).rstrip('/')

def pathjoin(*parts, **kvs):
    '''join path parts into a path; in case url is not none, use that, too'''
    url = kvs.pop('url', '/')
    url = url + '/' + '/'.join(parts)
    url = normalize_url(url)
    return url
