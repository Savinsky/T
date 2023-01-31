import random
from collections import Counter

n = 100
lst = ['Nikita', 'Alex', 'Peter', 'Kate', 'Jonh', 'Fox', 'Mike', 'Max', 'Any', 'Marta',
       'Phill', 'Bob', 'Jim', 'Donald', 'Kim', 'Sasha', 'Andrew', 'Garry', 'Joe', 'Moon']
def f(lst, n):
    l = []
    for i in range(n):
        l.append(random.choice(lst))
    return l
def most_common(lst):
    data = Counter(lst)
    return data.most_common(1)

def rar_letter(lst):
    b = [i[0] for i in lst]
    k = Counter(b)
    return min(k, key=k.get)

l = f(lst, n)
print(l)
print(most_common(l))
print(rar_letter(l))


