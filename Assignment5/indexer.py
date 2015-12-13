__author__ = 'pooja'

import pickle
import shelve
import urllib.request
from urllib.error import  URLError
import re

mapping = {}
s = shelve.open("myQuotes")

def indexFile():
    f = open("raw_data.pickle" , "br")
    data_list = pickle.load(f)
    for data in data_list:
        words = set(data[1].split())
        for word in words:
            if word in mapping.keys():
                mapping[word].add(data[0])
            else:
                mapping[word] = {data[0]}

#Crawl UNH site
def visit_url(url, domain):
    global crawler_backlog
    if(len(crawler_backlog)>100):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        print("Processing:", url)
    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            regexp_title = re.compile('<title>(?P<title>(.*))</title>')
            regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
            regexp_url = re.compile("http://"+domain+"[/\w+]*")

            result = regexp_title.search(content_string, re.IGNORECASE)
            if result:
                title = result.group("title")
                print(title.split(","))

            result = regexp_keywords.search(content_string, re.IGNORECASE)
            if result:
                keywords = result.group("keywords")
                print(keywords.split(","))

            for (urls) in re.findall(regexp_url, content_string):
                if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                    crawler_backlog[urls] = 0
                    visit_url(urls, domain)

    except URLError as e:
        print("error")

crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu")

for item in mapping.items():
    print(item)
    s[item[0]] = item[1]

'''
 for word in title.split(","):
                    if word in mapping.keys():
                        mapping[word].add(url)
                    else:
                        mapping[word] = {url}
'''

