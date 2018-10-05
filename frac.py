def gcd(m,n):
    while m %n != 0 :
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__ (self, numerator, denominator):
        if not(isinstance(numerator, int) and isinstance(denominator,int)):
            raise Exception("Error - numerator denominator not integers!")

        common = gcd(numerator, denominator)
        self.numerator = numerator//common
        self.denominator = denominator//common

    def show(self):
        print("In show")
        print(self.numerator, "/", self.denominator)

    def __str__(self):
        return(str(self.numerator) + "/" + str(self.denominator))

    def __add__(self, secobject):
        newnum = (self.numerator*secobject.denominator)+(secobject.numerator*self.denominator)
        newden = self.denominator*secobject.denominator
        common = gcd(newnum, newden)
        return Fraction(newnum,newden)

    def __sub__(self, secobject):
        newnum = (self.numerator*secobject.denominator)-(secobject.numerator*self.denominator)
        newden = self.denominator*secobject.denominator
        common = gcd(newnum, newden)
        return Fraction(newnum,newden)

    def __mul__(self, secobject):
        newnum = self.numerator*secobject.numerator
        newden = self.denominator*secobject.denominator
        common = gcd(newnum, newden)
        return Fraction(newnum,newden)

    def __eq__(self, secobject):
        if self.numerator == secobject.numerator and self.denominator == secobject.denominator :
            return 1
        return 0

    def __iadd__(self, secobject):
        newnum = (self.numerator * secobject.denominator) + (secobject.numerator * self.denominator)
        newden = self.denominator * secobject.denominator
        self.numerator = newnum
        self.denominator = newden


    def getNum(self):
        return self.numerator

    def getDen(self):
        return self.denominator

a = 'vasu'
fr = Fraction(a, 4)
fr2 = Fraction(14, 2)
print(fr+fr2)
