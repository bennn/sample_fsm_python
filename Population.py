from Utilities import choose_randomly
from Automata import Automaton
from retic import List
from copy import copy
from random import randrange


#TODO: add type to variable
data = (list(map(int, [line.strip() for line in open(
    "/Users/zeinamigeed/sample_fsm_python/population-random-numbers.txt")])))
rand_num = (element for element in data)

class Population:
    """
    Populations of Automata
    """
    #TODO: cannot add a return type due to bug
    def __init__(self, a: List(Automaton)):
        self.a = a
        self.b = [copy(x) for x in a]

    def payoffs(self):
        result = []
        for element in self.a:
            result = result + [element.pay()]
        return result

    #TODO: cannot add return type due to bug
    def match_up(self, r: int):
        """
        matches up neighboring pairs of
        automata in this population for r rounds
        :return: Population
        """
        self.reset()
        for i in range(0, len(self.a) - 1, 2):
            p1 = self.a[i]
            p2 = self.a[i+1]
            [a1, a2] = p1.interact(p2, r)
            self.a[i] = a1
            self.a[i+1] = a2
        return self

    #TODO: cannot add return type due to bug
    def regenerate(self, rate: int):
        """
        Replaces r elements of p with r 'children' of randomly chosen
        fittest elements of p, also shuffle constraint (r < (len p))
        :param rate: Number of elements to replace in a
        :param q: threshold
        :return: Population
        """
        payoffs = self.payoffs()
        substitutes = choose_randomly(payoffs, rate)
        # clone all automata in a at substitues
        # then "move" these clones into the first "rate" slots of a
        for i in range(rate):
            index = substitutes[i]
            self.a[i] = copy(self.b[index])
        self.shuffle()
        return self

    #TODO: add types to void
    def shuffle(self):
        self.b = [copy(x) for x in self.a]
        for i in range(len(self.a)):
            #j = randrange(i + 1)
            j = next(rand_num)
            if j != i:
                self.b[i] = self.b[j]
            self.b[j] = self.a[i]
        tmp = [copy(x) for x in self.a]
        self.a = [copy(x) for x in self.b]
        self.b = tmp

    #TODO: program crashes when adding a void return type
    def reset(self):
        """
        Reset all automata in a
        :return: None
        """
        for element in self.a:
            element.reset()
