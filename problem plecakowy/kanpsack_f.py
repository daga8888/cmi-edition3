items = [ ['a', 2, 4] , ['b', 4, 2] , ['c', 2, 2], ['d', 3, 3], ['e', 4, 1] ]

size = 6

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def knapsack_full(items, size):
    max_combination = None
    max_value = 0

    def value_and_weight(combination):
        value = 0
        weight = 0
        for item in combination:
            value += item[1]
            weight += item[2]
        return value, weight

    for combination in powerset(items):
        value, weight = value_and_weight(combination)
        if weight > size:
            continue
        if value > max_value:
            max_value = value
            max_combination = combination
    return max_combination

print(knapsack_full(items, size))