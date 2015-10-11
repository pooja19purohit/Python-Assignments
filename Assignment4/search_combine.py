__author__ = 'pooja'

import data_load
import indexer
import search

userInput = input("query:")
query = set(userInput.split(" "))

search.keySearch(query)
