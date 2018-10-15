from functools import reduce

a = ['agfkd.,f', 'Qksdf;sb&..', 'asdoo*', 'bgf...d', 're54()kj[]].']
b = (list(map (lambda x: x.count("."), a)))
print (b)
c = list(map(lambda p: p[0], filter(lambda x: x[1] > 2, zip(a, b))))
print (c)