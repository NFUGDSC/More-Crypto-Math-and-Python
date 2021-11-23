from Crypto.Util import number
# from sympy import *
# nextprime(123)

#1 隨意選擇兩個大的質數p和q，p不等於q，計算N=p*q;
p=number.getPrime(50)
q=number.getPrime(50)
N=p*q
print(f'{p}x{q}={N}')

#2 根據歐拉函數獲取phi
#phi = φ(N) = φ(p)φ(q) = (p-1)(q-1)。
phi=(p-1)*(q-1)

#3 選擇一個小於phi並與phi互質的整數e(public key) e我們通常取65537。
e = number.getPrime(80)
print(f'GCD({e},{phi})={number.GCD(e,phi)}')

#4 求得e關於phi的模反元素d(private key)
d=number.inverse(e,phi)
print(f'{e}*{d}%{phi}={e*d%phi}')
print(d)

P = b'SCIENCE'
P=number.bytes_to_long(P)
print(P)
print(C:=pow(P,e,N))
print(number.long_to_bytes(pow(C, d, N)))

# 加密: M ^ e = C(mod N)
# 解密: C ^ d = M(mod N)
# 公鑰: (N , e)
# 私鑰: (N , d)
