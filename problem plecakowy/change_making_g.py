K = 132

nominaly = [1, 2, 5, 10, 20, 50]

def change_making_greedy(K, nominaly):
    nominaly.sort(reverse = True)
    coins = []
    for i in nominaly:
        while K >= i:
            coins.append(i)
            K -= i
    return coins

print(change_making_greedy(K,nominaly))