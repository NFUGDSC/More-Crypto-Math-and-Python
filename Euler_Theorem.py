def gcd(a,b):
    if not b:
        return a
    return gcd(b,a%b)

def phi(n):
    x=0
    for i in range(n):
        if gcd(i,n)==1:
            x+=1
    return x

def euler(a, n):
    x = phi(n)
    return pow(a,x-1,n)#inverse

