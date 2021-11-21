def exgcd(a, n):
    if a == 0:
        return (n, 0, 1)
    else:
        g, x, y = exgcd(n % a, a)
        return (g, y - (n // a) * x, x)

def gcd(a,b):
    if not b:
        return a
    return gcd(b,a%b)

def modinv(a, n):
    g, x, y = exgcd(a, n)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % n
