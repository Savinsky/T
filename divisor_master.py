from collections import Counter
#1
def prime_number(n):
    k = 0
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False

#2
def number_divisors(n):
    numb_div = [d for d in range(1, n // 2 + 1) if n % d == 0] + [n]
    return numb_div

#3
def max_prime_divider(n):
    pr_div = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            pr_div.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        pr_div.append(n)
    return max(pr_div)

#4
def prime_multiplier(n):
    dict_degree = {
        0: "\u2070",
        1: "",
        2: "\u00B2",
        3: "\u00B3",
        4: "\u2074",
        5: "\u2075",
        6: "\u2076",
        7: "\u2077",
        8: "\u2078",
        9: "\u2079",
        10: "\u00B9" + "\u2070",
        11: "\u00B9" + "\u00B9"
    }
    i = 2
    prim = []
    while i * i <= n:
        while n % i == 0:
            prim.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        prim.append(n)
    prim = Counter(prim)
    res = {key: dict_degree.get(key, prim[key]) for key in prim}
    #for key, value in res.iteritems():
    #    print(res.get(key,value))
    return res

#5
def max_divider(n):
    return max(number_divisors(n))

print prime_number(100)
print number_divisors(100)
print max_prime_divider(100)
print prime_multiplier(100)
print max_divider(100)