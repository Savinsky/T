import random
from collections import Counter

n = 10
lst = ['Nikita', 'Alex', 'Peter', 'Kate', 'Jonh', 'Fox', 'Mike', 'Max', 'Any', 'Marta',
       'Phill', 'Bob', 'Jim', 'Donald', 'Kim', 'Sasha', 'Andrew', 'Garry', 'Joe', 'Moon']
def f(lst, n):
    l = []
    for i in range(n):
        l.append(random.choice(lst))
    return l
def most_common(lst):
    max = 0
    result = None
    for x in set(lst):
        count = lst.count(x)
        if count > max:
            max = count
            result = x
    return result
    #data = Counter(lst)
    #return data.most_common(1)[0][0]

l = f(lst, n)
print(l)
print(most_common(l))


