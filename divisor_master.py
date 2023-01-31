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
   i = 2
   prim = []
   while i * i <= n:
       while n % i == 0:
           prim.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       prim.append(n)
   return prim

#5
def max_divider(n):
    return max(number_divisors(n))

print prime_number(100)
print number_divisors(100)
print max_prime_divider(100)
print prime_multiplier(100)
print max_divider(100)