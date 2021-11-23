from sympy import Matrix #pip install sympy
import numpy as np

def HillCipherEncrypto(P,Key):
    P=P.replace(' ','').lower()
    Parray=[]
    if len(P)%2==1:
        P+='z'
    for i in range(len(P)):
        Parray.append(ord(P[i])-ord('a'))

    Parray=np.array(Parray).reshape(len(P)//len(K),len(K))
    Key=np.array(Key)
    Carray=np.mod(Parray.dot(Key),26)
    C=''
    for i in range(len(Carray)):
        for j in range(len(Carray[i])):
            C+=chr((Carray[i][j]%26+ord('a')))
    return C


def HillCipherDecrypto(C, Key):
    Keyinv = np.array(Matrix(Key).inv_mod(26))
    Carray=[]
    for i in range(len(C)):
        Carray.append(ord(C[i])-ord('a'))
    Carray=np.mod(np.array(Carray).reshape(len(C)//len(Key),len(Key)).dot(Keyinv),26).flatten()
    P=''
    for i in Carray:
        P+=chr(i+ord('a'))
    return P
