from retic import List
from bisect import bisect
from random import random
from pip._vendor.requests.packages.urllib3.connectionpool import xrange


#TODO: add type to variable
data = (list(map(float, [line.strip() for line in open("random-numbers.txt")])))
rand_num = (element for element in data)


def accumulated_s(probabilities):
    total = sum(probabilities)
    payoffs = probabilities
    result = []
    next = 0
    for element in payoffs:
        next += element
        result = result + [next/total]
    return result

def choose_randomly(probabilities, speed):
    s = accumulated_s(probabilities)
    res = []  ### changed here
    for n in range(speed):
        #r = random()
        r = next(rand_num)
        for i in range(len(s)):
            if r < s[i]:
                res = [i] + res  ### and here
                break
    return res  ### and here


def relative_average(l: List(float), w: float) -> float:
    return sum(l) / w / len(l)