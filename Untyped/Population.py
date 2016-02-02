from retic import List, Void
from Untyped.Utilities import choose_randomly
from Untyped.Automata import Automaton
from copy import copy

#TODO: cannot type a variable in retic
data = (list(map(int, [line.strip() for line in open(
    "/Users/zeinamigeed/sample_fsm_python/population-random-numbers.txt")])))
rand_num = (element for element in data)

class Population:
    """
    Populations of Automata
    """

    def __init__(self, a):
        self.a = a

    def payoffs(self):
        result = []
        for element in self.a:
            result = result + [element.pay()]
        return result

    def match_up(self, r):
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

    def regenerate(self, rate):
        """
        Replaces r elements of p with r 'children' of randomly chosen
        fittest elements of p, also shuffle constraint (r < (len p))
        :param rate: Number of elements to replace in a
        :param q: threshold
        :return: Population
        """
        payoffs = self.payoffs()
        substitutes = choose_randomly(payoffs, rate)
        for i in range(rate):
            index = substitutes[i]
            self.a[i] = self.a[index].clone()
        self.shuffle()
        return self

    def shuffle(self):
        b = copy(self.a)
        for i in range(len(self.a)):
            j = next(rand_num)
            if j != i:
                b[i] = b[j]
            b[j] = self.a[i]
        self.a = b

    def reset(self):
        """
        Reset all automata in a
        :return: None
        """
        self.a = [element.reset() for element in self.a]



