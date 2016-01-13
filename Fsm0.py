from Utilities import relative_average
from Other import build_random_population
from retic import List

def run() -> List(List(float)):
    simulation_to_lines(evolve(build_random_population(100), 1000, 10, 20))

def evolve(p, c: int, s: int, r: int) -> List(float):
    """
    Computes the list of average payoffs over the evolution of population
    p for c cycles of match_ups with r rounds per match and at birth/death
    rate of s
    :param p: Population
    :param c: Natural
    :param s: Natural
    :param r: Natural
    :return: [float]
    """
    payoffs = []
    for i in range(c):
        p2 = p.match_up(r)
        pp = p2.payoffs()
        p3 = p2.regenerate(s)

        payoffs = [relative_average(pp, r)] + payoffs
        p = p3

    return payoffs

#TODO: Adding a void return type crashes program
def simulation_to_lines(data: List(float)):
    """
    Turn average payoffs into a list of Cartesian points
    :param data: [Payoffs]
    :return: [[x, y], ..]
    """
    result = []
    counter = 0
    for payoff in data:
        result = result + [[counter, payoff]]
        counter+=1

    print(str(result))


run()