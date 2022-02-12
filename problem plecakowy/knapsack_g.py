items = [ ['a', 2, 4] , ['b', 4, 2] , ['c', 2, 2], ['d', 3, 3], ['e', 4, 1] ]

size = 6
import copy

def knapsack_greedy(items, size):
    inner_items = copy.deepcopy(items)
    for item in inner_items:
        item.append(item[1]/item[2])
    inner_items.sort(key=lambda x : x[3], reverse = True)
    knapsack = {}
    for item in inner_items:
        if item[2] <= size:
            size -= item[2]
            knapsack[item[0]] = item[:]
    return knapsack

print(knapsack_greedy(items, size))