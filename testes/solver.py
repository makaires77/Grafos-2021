from core import *


class SolveState:
    def __init__(self):
        self.best_path = math.pow(2, 32)
        self.finished = False


def compare_current_with_best_path(cities, state):
    current_is_better = False
    distance = calc_path_distance(cities)
    if state.best_path > distance:
        state.best_path = distance
        current_is_better = True
    return current_is_better


def solve_random_step(cities, state):
    random.shuffle(cities)
    return compare_current_with_best_path(cities, state)


def solve_lexicographic_symmetric_step(cities, state):
    is_over = lexicographic_execution(cities)
    while is_path_duplicated(cities) and not is_over:
        is_over = lexicographic_execution(cities)
    if is_over:
        state.finished = True
    return compare_current_with_best_path(cities, state)


def is_path_duplicated(cities):
    result = False
    if cities[1].number > cities[len(cities) - 1].number:
        result = True
    return result