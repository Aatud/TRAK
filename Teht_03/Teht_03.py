def reku(n):
    if n==0:
        print "ei kutsua"
        return 1
    else:
        print "uusi kutsu"
        return float(1/(1+reku(n-1)))

print reku(0)
print reku(1)
print reku(2)
print reku(3)
print reku(4)
print reku(5)
