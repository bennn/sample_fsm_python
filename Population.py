from Utilities import choose_randomly
from Automata import Automaton
from retic import List
from random import randrange
from Utilities import rand_num

class Population:
    """
    Populations of Automata
    """
    #TODO: cannot add a return type due to bug
    def __init__(self, a: List(Automaton)):
        self.a = a

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
        for i in range(0, round(len(self.a)/2)):
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
        b = self.a.copy()
        # then "move" these clones into the first "rate" slots of a
        for i in range(rate):
            index = substitutes[i]
            self.a[i] = b[index]
        self.shuffle()
        return self

    #TODO: add types to void
    def shuffle(self):
        res = self.a
        for i in range(len(self.a)):
            j = randrange(i + 1)
            #j = next(rand_num)
            if j != 1:
                res[i], res[j] = res[j], res[i]
            self.a = res

    #TODO: program crashes when adding a void return type
    def reset(self):
        """
        Reset all automata in a
        :return: None
        """
        for element in self.a:
            element.reset()
