from logic_gate import *
from half_adder import HalfAdder
#Watch this video if it makes no sense -> singular binary adder
#https://www.youtube.com/watch?v=VPw9vPN-3ac


class FullAdder(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        
        #first half adder
        self.xor_primary_gate = XorGate("xor_prim")
        self.and_primary_gate = AndGate("and_prim")

        #Second half adder
        self.xor_secondary_gate = XorGate("xor_sec")
        self.and_secondary_gate = AndGate("and_sec")

        #Binary adder for 2-3 binarys (1,1,0 : 1,0,1 : 0,1,1 : 1,1,1)
        self.or_carry_gate = OrGate("or_carry")

        self.pinA = None
        self.pinB = None
        self.carry = None
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
        
    def getPinCarry(self):
        if self.carry is None:
            return int(input("Enter Carry_in input for gate "+self.getLabel()+"-->"))
        elif self.carry in self.binary_inputs:
            return self.carry
        elif isinstance(self.carry, Connector):
            return self.carry.getFrom().getOutput()
        else:
            raise ValueError("Your Carry is not of valid type") 

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        c_in = self.getPinCarry()


        #primary_half_adder
        self.xor_primary_gate.pinA = a
        self.xor_primary_gate.pinB = b
        self.and_primary_gate.pinA = a
        self.and_primary_gate.pinB = b

        #Secondary_half_Adder
        self.xor_secondary_gate.pinA = self.xor_primary_gate.getOutput()
        self.xor_secondary_gate.pinB = c_in
        self.and_secondary_gate.pinA = self.xor_primary_gate.getOutput()
        self.and_secondary_gate.pinB = c_in

        #Rogue or_gate
        self.or_carry_gate.pinA = self.and_primary_gate.getOutput()
        self.or_carry_gate.pinB = self.and_secondary_gate.getOutput()

        #Outputs
        gate_sum = self.xor_secondary_gate.getOutput()
        gate_carry = self.or_carry_gate.getOutput()

        print(f"sum = {gate_sum} and carry = {gate_carry}")
 
        return gate_sum, gate_carry
    

#try with two half adders and this rogue or gate.
class FullAdderInherit(HalfAdder):
    def __init__(self, label):
        super().__init__(label)
        pass

if __name__ == "__main__":
    h1 = FullAdder("H_full_1")
    h1_output = h1.getOutput()
    print(h1_output)
    print(type(h1_output))









