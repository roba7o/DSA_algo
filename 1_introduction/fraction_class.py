def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num,new_den)
        return Fraction(new_num//common,new_den//common)
       
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num,new_den)
        return Fraction(new_num//common,new_den//common)
    
    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    
    def __gt__(self, other):
        return (self.num * other.den) > (other.num * self.den)
    
    def __lt__(self, other):
        return (self.num * other.den) < (other.num * self.den)
            

x = Fraction(1,2)
y = Fraction(2,3)

print(x.getDen())
print(x.getNum())
print(x+y)
print(x == y)
print(y*x)
print(y/x)
