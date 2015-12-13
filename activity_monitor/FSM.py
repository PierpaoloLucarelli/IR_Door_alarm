''' 
Author : Pierpaolo Lucarelli 
MonitorFSM class taht extends the FSM class.
this class ir sesponsible for handling the I/O of the machine
Give a certain type of input and the correct type of output will be send
'''
class FSM:
    def start(self):
        self.state = self.startState
    # now prompt the FSM to step to its next state
    # return output prompted by this transition
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        # print (s)
        return o
    # method used for testing the FSM implementation
    # method must be invoked with a list of inputs
    # returns a list of total state descriptors
    # where total state is a tuple comprising:
    # input
    # output
    # next state
    def transduce(self, inputs):
        # initialise the FSM
        # now run FSM through a serious of state changes
        # prompted by inputs to the FSM
        return [(str(inp), self.step(inp), self.state) \
                for inp in inputs]
    
