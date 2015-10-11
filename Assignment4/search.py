__author__ = 'pooja'
from _datetime import datetime
from data_load import data_list
from indexer import index
import shelve

#index()

mapping = shelve.open("myQuotes")

def keySearch(query):
    if("or" in query and "and" not in query):
        query.remove("or")
        print("Performing OR search for " + str(query))
        results = set()
        for queryWord in query:
            if queryWord in mapping.keys():
                results = results.union(mapping[queryWord])
        for result in results:
            print("Found at ", result)

    else:
        if("and" in query):
            query.remove("and")
        if("or" in query):
            query.remove("or")
        print("Performing AND search for " + str(query))
        results = {}
        for i,queryWord in enumerate(list(query)):
            if queryWord in mapping.keys():
                if i ==0:
                    results = mapping[queryWord]
                else:
                    results = results & mapping[queryWord]
        for result in results:
            print("Found at ", result)