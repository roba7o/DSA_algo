def gcd(m,n):
    """
    Using Euclids Algorithm 
    m = n.Q + R
    n = R.newQ + newR

    It breaks down the until the remainder can divide into the new n. 
    When there is none this will be 1 (two relative primes/coprime)

    Parameters:
    - m (int): The first integer.
    - n (int): The second integer.

    Returns:
    returns int: previous m where the r=0 --> n=0 and loop breaks gcd
    """
    if n == 0 or m == 0:
        return None

    while n != 0:
        r = m % n  # Calculate the remainder
        m = n      # Update m to be the old n
        n = r      # Update n to be the remainder
    return m


class Fraction:
    def __init__(self,top,bottom):
         self.num = top/gcd(top,bottom)
         self.den = bottom/gcd(top,bottom)
         
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
