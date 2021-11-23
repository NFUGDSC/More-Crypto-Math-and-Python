
def PlayfairCipherEncrypto(P, Key):
    key = Key
    Key = []
    k = 0
    check = []
    for i in range(5):
        Key.append([])
        for j in range(5):
            if k < len(key):
                Key[i].append(key[k])
                check.append(key[k])
                k += 1
            else:
                for l in range(26):
                    alpha = chr(l+ord('a'))
                    if alpha == 'i' or alpha == 'j':
                        alpha = 'i'
                    if alpha not in check:
                        Key[i].append(alpha)
                        check.append(alpha)
                        break

    C = ""
    couple = []
    P = P.replace(' ', '')
    i = 0
    while(i < len(P)):
        if i+1 < len(P):
            if P[i] != P[i+1]:
                couple.append(P[i])
                couple.append(P[i+1])
                i += 2
            else:
                couple.append(P[i])
                couple.append("x")
                i += 1
        else:
            couple.append(P[i])
            i += 1
    if len(couple) % 2 == 1:
        couple.append('x')

    for i in range(0, len(couple), 2):
        for j in range(5):
            if couple[i] in set(Key[j]):
                if couple[i+1] in set(Key[j]):  # row
                    for l in range(2):
                        for k in range(5):
                            if couple[i+l] == Key[j][k]:
                                C += Key[j][(k+1) % 5]
                                break
                else:
                    x = 0
                    for k in range(5):
                        if couple[i] == Key[j][k]:
                            x = k
                            break
                    for l in range(5):  # col
                        if couple[i+1] in set(Key[l]):
                            for k in range(5):
                                if couple[i+1] == Key[l][k]:
                                    if x == k:
                                        C += Key[(j+1) % 26][k]
                                        C += Key[(l+1) % 26][k]
                                        break
                                    else:
                                        C += Key[j][k]
                                        C += Key[l][x]
                                        break
    return C

def PlayfairCipherDecrypto(P, Key):
    Key = []
    k = 0
    check = []
    for i in range(5):
        Key.append([])
        for j in range(5):
            if k < len(key):
                Key[i].append(key[k])
                check.append(key[k])
                k += 1
            else:
                for l in range(26):
                    alpha = chr(l+ord('a'))
                    if alpha == 'i' or alpha == 'j':
                        alpha = 'i'
                    if alpha not in check:
                        Key[i].append(alpha)
                        check.append(alpha)
                        break
    couple=[]
    for i in range(0,len(C),2):
        couple.append([C[i],C[i+1]])
    P=''
    for i in couple:
        for j in range(5):
            if i[0] in Key[j]:
                if i[1] in Key[j]:
                    for g in i:
                        for k in range(5):
                            if g==Key[j][k]:
                                P+=Key[j][(k-1)%5]
                                break
                else:
                    x=0
                    for k in range(5):
                        if i[0]==Key[j][k]:
                            x=k
                            break
                    for k in range(5):
                        if i[1] in Key[k]:
                            for l in range(5):
                                if i[1] == Key[k][l]:
                                    if i[0] == Key[j][l]:
                                        P += Key[(j-1)%5][l]
                                        P += Key[(k-1)%5][l]
                                        print(i)
                                        break
                                    else:
                                        P += Key[j][l]
                                        P += Key[k][x]
                                        break
    return P
