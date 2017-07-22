from functions import comb as get_combinations

a = ['1','2']
b = ['3','4']

combs = [[x+y for y in get_combinations(b)] for x in get_combinations(a)]
combs = combs[0] + combs[1]

print(combs)
