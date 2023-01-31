def prime_number(n):
    k = 0
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False

def number_divisors(n):
    numb_div = [d for d in range(1, n // 2 + 1) if n % d == 0] + [n]
    return numb_div

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

print prime_number(100)
print number_divisors(100)
print max_prime_divider(100)