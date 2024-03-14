from logic_gate import BinaryGate

class HalfAdder(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a ==1 and b==1:
            SUM = 0
        elif (a ==0 and b==1) or (a==1 and b==0):
            SUM = 1
        else:
            SUM = 0
        if a==1 and b==1:
            CARRY = 1
        else:
            CARRY = 0
        return SUM, CARRY

def main():
    h1 = HalfAdder("H1")
    print(h1.getOutput())

if __name__ == "__main__":
    main()

