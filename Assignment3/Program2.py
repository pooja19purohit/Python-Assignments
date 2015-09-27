__author__ = 'pooja'


def count_frequency(input):
    count = {}
    for word in input:
        if word in count.keys():
            count[word] += 1
        else:
            count[word] = 1
    return count


mylist = ["one", "two", "eleven", "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist))
