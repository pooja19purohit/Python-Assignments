__author__ = 'pooja'

import data_load
import pickle
import shelve

mapping = {}
s = shelve.open("myQuotes")

def index():
    f = open("raw_data.pickle" , "br")
    data_list = pickle.load(f)
    for data in data_list:
        words = set(data[1].split())
        for word in words:
            if word in mapping.keys():
                mapping[word].add(data[0])
            else:
                mapping[word] = {data[0]}

    for item in mapping.items():
        s[item[0]] = item[1]



    '''for i,quote in enumerate(data_load.data_list):
        words = set(quote.split())
        for word in words:
            if word in mapping.keys():
                mapping[word].add(i)
            else:
                mapping[word] = {i}'''