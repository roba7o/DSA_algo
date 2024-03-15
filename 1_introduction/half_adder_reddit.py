#1) Create new adder class entirely and inherit
#2) Overide setNextPin (its not a standard output gate)

from logic_gate import BinaryGate, AndGate, XorGate

#1 )Override -> Reuses Code but isnt technically standard gate as outputs tuple
class HalfAdderInherit(BinaryGate):
    def __init__(self,label):
        BinaryGate.__init__(self,label)

        self.xor_gate = XorGate("xor1")
        self.and_gate = AndGate("and1")

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        #potentially introduce instance(?) method
        self.xor_gate.pinA = a
        self.xor_gate.pinB = b
        self.and_gate.pinA = a
        self.and_gate.pinB = b

        gate_sum = self.xor_gate.getOutput()
        gate_carry = self.and_gate.getOutput()

        print(f"sum = {gate_sum} and carry = {gate_carry}")
 
        return gate_sum, gate_carry
    
#1 )Override -> Reuses Code but isnt technically standard gate as outputs tuple
class HalfAdderOverride(BinaryGate):
    def __init__(self,label):
        BinaryGate.__init__(self,label)
        pass


if __name__ == "__main__":
    h1 = HalfAdderInherit("H1")
    h1_output = h1.getOutput()
    print(h1_output)
    print(type(h1_output))
        



    


    