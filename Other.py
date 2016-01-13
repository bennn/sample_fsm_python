from Automata import Automaton
from Population import Population
from random import randrange
from Utilities import rand_num

def make_random_automaton(n: int):
    """
    builds an n states x k inputs automation
    with a random transition table
    :param n:
    :return: Automation
    """
    seed = randrange(n)
    #seed = (next(rand_num))

    table = []
    for i in range(n):
        trans = [randrange(n) for i in range(n)]
        #trans = [(next(rand_num)) for i in range(n)]
        table = table + [trans]
    return Automaton(seed, 0, table, seed)


#TODO: cannot add return type due to bug
def build_random_population(n: int):
    """
    for even n, build a population of size n
    :param n: Natural
    :return: Population
    """
    DEF_COO = 2
    v = []
    for i in range(n):
        v = v + [make_random_automaton(DEF_COO)]
    return Population(v)




