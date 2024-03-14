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
        # self.num= top
        # self.den = bottom

        if isinstance(top, int):
            self.num= top
        else:
            raise ValueError("Top isn't an int")
            
        if isinstance(bottom, int):
            self.den = bottom
        else:
            raise ValueError("bottom isn't an int")
        
        if self.den < 0 and self.num > 0:
            self.den = -self.den
            self.num = -self.num

        common = gcd(self.num,self.den)
        self.num = self.num//common
        self.den = self.den//common
    
    #Getters
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den

    #Prints
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __repr__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    #relational
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    
    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum
    
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum
    
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum
    
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum
    
    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    #Computational
    def __add__(self,other):
        if (isinstance(other, int)):
            other = Fraction(1,1)
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    #You want this if the left side (self) is a integer
    # a + b == b + a when a or b == int or fraction
    def __radd__(self, other):
        return self.__add__(other)
    
    def __iadd__(self, other):
        self = self.__add__(other)
        return self


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
#string functions
print(f"x is {x}")
print("y is {}".format(y))

#getters
print(f"x num = {x.getNum()}")
print(f"x den = {x.getDen()}")

#normal add
print(f"x+y--> {x+y}")

#add integer and also radd
print(f"x+1--> {x+1}")
print(f"1+x--> {1+x}")

#iadd
print(f"x is {x}")
print("y is {}".format(y))
x += y
print(f"iadd fucntion: x += y")
print(f"x is now {x}")
print("y is still  {}".format(y))

#standard ones
print(x == y)
print(y*x)
print(y/x)
