from retic import List

import os, sys
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '..'))

#TODO: Cannot type variable in retic
data = (list(map(int, [line.strip() for line in open(
    "utill-random-numbers.txt")])))
rand_num = (element for element in data)


def accumulated_s(probabilities:List(float))->List(float):
    total = sum(probabilities)
    payoffs = probabilities
    result = []
    next = 0
    for element in payoffs:
        next += element
        result = result + [next/total]
    return result

def choose_randomly(probabilities:List(float), speed:int)->List(int):

    s = accumulated_s(probabilities)
    res = []  ### changed here
    for n in range(speed):
        #r = random()
        r = next(rand_num)
        for i in range(len(s)):
            if r < s[i]:
                res = res + [i]   ### and here
                break
    return res  ### and here


def relative_average(l: List(float), w: float) -> float:
    return sum(l) / w / len(l)

