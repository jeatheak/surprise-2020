

class StateMachine:
    def __init__(self, annotate: int = 0):
        self.state = 0
        self.__annotate = annotate
        self.transitions = list()

    def checkState(self) -> None:
        if self.state < len(self.transitions):
            self.nextState(self.transitions[self.state])
        else: print(self.state, ' Do nothing')

    def nextState(self, input = True) -> None:
        if input:
            self.state += 1
            if self.__annotate: print(self.state, ' Going to next Stage')
        else:
            if self.__annotate: print(self.state, ' False Input')
    
    def setState(self, input, state):
        if input:
            self.state = state
    
    def reset(self):
        self.state = 0

    def add(self, input) -> None:
        self.transitions.append(input)



# test = StateMachine(1)

# def testFunction(input: int) -> int:
#     if input: return 1
#     else: return 0

# test.transitions.append(testFunction(1))
# test.transitions.append(testFunction(0))
# test.transitions.append(testFunction(1))
# test.transitions.append(1)

# test.checkState()
# test.checkState()
# test.checkState()
# test.transitions[1] = testFunction(1)
# test.checkState()
# test.checkState()
# test.checkState()
# test.checkState()
# test.checkState()
# test.checkState()
# test.checkState()