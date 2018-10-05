class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return(int(input("Enter the input pinA for gate "+ self.getLabel()+"-->")))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return(int(input("Enter the input pinB for gate "+ self.getLabel()+"-->" )))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            return RuntimeError("Error: No Empty Pins")

class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return(int(input("Enter the input pin for gate " + self.getLabel() + "-->")))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            return RuntimeError("Error: No Empty Pin")

class ANDGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1 :
            return 1
        return 0

class NANDGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1 :
            return 0
        return 1

class NORGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0 :
            return 1
        return 0

class XORGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and not b == 1 :
            return 1
        elif not a == 1 and b == 1:
            return 1
        return 0

class ORGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinB()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        return 1

class NOTGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
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


g1 = ANDGate("a1")
g2 = XORGate("x1")
c = g1.getOutput()
s =  g2.getOutput()
