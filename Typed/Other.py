from Population import Population
from Automata import Automaton
from random import randrange
from Timer import data_path

#TODO: Cannot type variable in retic
data = (list(map(int, [line.strip() for line in
    open(data_path("automata-random-numbers.txt"))])))
rand_num = (element for element in data)


def make_random_automaton(n: int)->Automaton:
    """
    builds an n states x k inputs automation
    with a random transition table
    :param n:
    :return: Automation
    """
    seed = (next(rand_num))
    table = [[(next(rand_num)) for _ in range(n)] for _ in range(n)]
    return Automaton(seed, 0, table, seed)


def build_random_population(n: int)->Population:
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




