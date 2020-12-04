class StateMachine:
    def __init__(self, annotate: bool = False):
        self.state = 0
        self.__annotate = annotate
        self.transitions = list()

    def checkState(self) -> None:
        if self.state < len(self.transitions):
            # self.nextState(self.transitions[self.state])
            if self.transitions[self.state]():
                self.nextState()

    def nextState(self) -> None:
        self.state += 1
        if self.__annotate:
            print(self.state, ' Going to next Stage')

    def prevState(self) -> None:
        self.state -= 1
        if self.__annotate:
            print(self.state, ' Going to prev Stage')

    def setState(self, input, state):
        if input:
            self.state = state

    def reset(self):
        self.state = 0

    def add(self, input) -> None:
        self.transitions.append(input)


# == TESTS ==
# def test(st: StateMachine):
#     st.nextState()

# st = StateMachine(True)

# def tt():
#     return True


# st.add(lambda: tt())
# st.add(lambda: tt())
# st.add(lambda: test(st))

# while True:
#     st.checkState()
