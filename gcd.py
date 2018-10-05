def gcd(m,n):
    while m %n != 0 :
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

m = int(input("Enter 1st int: "))
n = int(input("Enter 2nd int: "))
print(gcd(m,n))
