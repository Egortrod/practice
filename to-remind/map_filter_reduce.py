from functools import reduce


def keep_truthful(data):
    return list(filter(None, data))


def abs_sum(data):
    return reduce(lambda x: sum(abs(x)), data)
    
##########################################################
from operator import getitem, truth

def keep_truthful(items):
    return filter(truth, items)


def abs_sum(numbers):
    return sum(map(abs, numbers))


def walk(dictionary, path):
    return reduce(getitem, path, dictionary) #!!!!!!!!!!!!!!!!!