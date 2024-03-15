class LogicGate:
    def __init__(self,label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,label):
        super(BinaryGate, self).__init__(label)
        self.pinA = None
        self.pinB = None
        self.binary_inputs = (1,0)

    
    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        elif self.pinA in self.binary_inputs:
            return self.pinA
        elif isinstance(self.pinA, Connector):
            return self.pinA.getFrom().getOutput()
        else:
            raise ValueError("Your pin is not of valid type")

    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        elif self.pinB in self.binary_inputs:
            return self.pinB
        elif isinstance(self.pinB, Connector):
            return self.pinB.getFrom().getOutput()
        else:
            raise ValueError("Your pin is not of valid type")


    def setNextPin(self,source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):
    def __init__(self,label):
        BinaryGate.__init__(self,label)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,label):
        BinaryGate.__init__(self,label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0
        
class NandGate(BinaryGate):
    def __init__(self,label):
        BinaryGate.__init__(self,label)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 1
        else:
            return 0

class NorGate(BinaryGate):

    def __init__(self,label):
        BinaryGate.__init__(self,label)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==0 or b==0:
            return 1
        else:
            return 0
        
class XorGate(BinaryGate):

    def __init__(self,label):
        BinaryGate.__init__(self,label)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==b:
            return 0
        else:
            return 1

class UnaryGate(LogicGate):
    def __init__(self,label):
        LogicGate.__init__(self,label)
        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate):
    def __init__(self,label):
        UnaryGate.__init__(self,label)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
    

def main():
    # Create gates
    g1 = NorGate("G1")
    g2 = NandGate("G2")
    g3 = AndGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)

    print(g4.getOutput())

if __name__ == "__main__":
    main()
