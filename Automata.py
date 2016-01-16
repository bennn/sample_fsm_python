from retic import List
from retic import Dyn
class Automaton:

    #TODO: Variables are not typed yet
    PAYOFF_TABLE = [[(3, 3), (0, 4)],
                    [(4, 0), (1, 1)]]

    #TODO: Should return an Automation. Bug preventing adding this type.
    def __init__(self, current: int,
                 payoff: float,
                 table: List(List(int)),
                 initial: int):
        self.current = current
        self.payoff = payoff
        self.table = table
        self.initial = initial

    def interact(self, other: Dyn, r: int) -> List:
        """
        the sum of pay-offs for the two respective automata over all rounds
        :param other: Automaton
        :param r: rounds
        :return: (Automaton)
        """
        c1 = self.current
        y1 = self.payoff
        t1 = self.table
        c2 = other.current
        y2 = other.payoff
        t2 = other.table

        for i in range(0, r):
            input = c2
            (p1, p2) = self.PAYOFF_TABLE[c1][input]

            c1 = t1[c1][input]
            y1 = y1 + p1
            c2 = t2[c2][c1]
            y2 = y2 + p2
        self.current = c1
        self.payoff = y1
        other.current = c2
        other.payoff = y2
        return [self, other]

    def pay(self) -> float:
        """
        reset the historic payoff
        :return: float
        """
        return self.payoff

    #TODO: cannot type due to bug
    def clone(self):
        """
        reset payoff and current state to initial strategy
        :return: Automaton
        """
        return Automaton(self.initial, 0, self.table, self.initial)

    #TODO: cannot type due to bug
    def reset(self):
        """
        reset the historic payoff
        :return: Automation
        """
        return Automaton(self.current, 0, self.table, self.initial)

    def compute_payoffs(self, other_current: int) -> List(float):
        """
        :param other_current: Natural
        :return: [Automaton]
        """
        return self.PAYOFF_TABLE[self.current][other_current]

    def __eq__(self, other: Dyn) -> bool:
        if not isinstance(other, Automaton):
            return False
        else:
            return (self.current == other.current and self.payoff ==
                    other.payoff and self.initial == other.initial and
                    self.table == other.table)

    def __str__(self):
        return str("current: %s payoff: %s " % \
               (self.current, self.payoff))
