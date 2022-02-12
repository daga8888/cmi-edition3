from typing import List
K = 132

nominaly = [1, 2, 5, 10, 20, 50]

def change_making_brute_firce(K : int, nominaly : List):
    nominaly_order_desc = sorted(nominaly, reverse=True)
    solutions = [ [] ]
    for nominal in nominaly_order_desc:
        tmp_solutions = solutions.copy()
        for solution in tmp_solutions:
            change = K - sum(solution)
            new_solutions = [ solution + [nominal for _ in range(i//nominal)] for i in range(0,change+1, nominal)]
            solutions.extend(new_solutions)
            solutions.remove(solution)
    true_solutions = []
    for solution in solutions:
        if sum(solution) == K:
            true_solutions.append(solution)
    return true_solutions
K = 132

nominaly = [1, 2, 5, 10, 20, 50]

print(change_making_brute_firce(K,nominaly))