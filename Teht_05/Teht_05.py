#a) Kaksi edellista arvoa lasketaan yhteen
#b)
def Fi(k):
    a = [0, 1]
    i = 0
    while i < k:
        a.append(a[0+i]+a[1+i])
        i = i+1
    return a[i]
print Fi(11)

#c)

def Fr(k):
    if k == 0:
        return 0
    if k <= 1:
        return 1
    else:
        return Fr(k-1)+Fr(k-2)
print Fr(11)
