from retic import List, Dyn, Void, String


class Automaton:
    PAYOFF_TABLE = [[(3, 3), (0, 4)], [(4, 0), (1, 1)]]

    def __init__(self: Automaton, current: int, payoff: float, table: List(
        List(int)), initial: int) ->Void:
        self.current = current
        self.payoff = payoff
        self.table = table
        self.initial = initial

    def interact(self, other, r):
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
            p1, p2 = self.PAYOFF_TABLE[c1][input]
            c1 = t1[c1][input]
            y1 = y1 + p1
            c2 = t2[c2][c1]
            y2 = y2 + p2
        self.current = c1
        self.payoff = y1
        other.current = c2
        other.payoff = y2
        return [self, other]

    def clone(self: Automaton) ->Automaton:
        """
        reset payoff and current state to initial strategy
        :return: Automaton
        """
        return Automaton(self.initial, 0, self.table, self.initial)

    def reset(self):
        """
        reset the historic payoff
        :return: Automation
        """
        return Automaton(self.current, 0, self.table, self.initial)

    def compute_payoffs(self: Automaton, other_current: int) ->List(float):
        """
        :param other_current: Natural
        :return: [Automaton]
        """
        return self.PAYOFF_TABLE[self.current][other_current]

