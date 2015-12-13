''' 
Author : Pierpaolo Lucarelli 
Tests for the activity monitor
'''
from MonitorFSM import *


def correct_code_sequence():
	print("correct code sequence test\n")
	# define list of inputs to test the FSM
	testInputs = ['Up', 'Down', 'Left', 'Right']
	# construct and initialise FSM
	ts = MonitorFSM()
	ts.start()
	# display start state
	print('Start state:', ts.state)
	# display all state transitions prompted by
	# the specified list of test inputs
	for total_state in ts.transduce(testInputs):
		# display input, output, next state
		print(('In: {0[0]:<20s}'+
			  'Out: {0[1]:<10s}'+
			  'Next state: {0[2]:<10s}')
			  .format(total_state))

def incorrect_code_sequence():
	print("incorrect code sequence test\n")
	# define list of inputs to test the FSM
	testInputs = ['Up', 'Down', 'key', 'Right']
	# construct and initialise FSM
	ts = MonitorFSM()
	ts.start()
	# display start state
	print('Start state:', ts.state)
	# display all state transitions prompted by
	# the specified list of test inputs
	for total_state in ts.transduce(testInputs):
		# display input, output, next state
		print(('In: {0[0]:<20s}'+
			  ' Out: {0[1]:<10s}'+
			  ' Next state: {0[2]:<10s}')
			  .format(total_state))


def correct_code_for_deactivating():
	print("correct code sequence for deactivating\n")
	# define list of inputs to test the FSM
	testInputs = ["Up", "Down", "Left", "Right"]
	# construct and initialise FSM
	ts = MonitorFSM()
	ts.start()
	ts.state = "activated"
	# display start state
	print('Start state:', ts.state)
	# display all state transitions prompted by
	# the specified list of test inputs
	for total_state in ts.transduce(testInputs):
		# display input, output, next state
		print(('In: {0[0]:<20s}'+
			  ' Out: {0[1]:<10s}'+
			  ' Next state: {0[2]:<10s}')
			  .format(total_state))	

def incorrect_code_for_deactivating():
	print("incorrect code sequence for deactivating\n")
	# define list of inputs to test the FSM
	testInputs = ["Up", "Down", "Up", "Right"]
	# construct and initialise FSM
	ts = MonitorFSM()
	ts.start()
	ts.state = "activated"
	# display start state
	print('Start state:', ts.state)
	# display all state transitions prompted by
	# the specified list of test inputs
	for total_state in ts.transduce(testInputs):
		# display input, output, next state
		print(('In: {0[0]:<20s}'+
			  ' Out: {0[1]:<10s}'+
			  ' Next state: {0[2]:<10s}')
			  .format(total_state))	

def take_pic_test():
	print("take picture test\n")
	# define list of inputs to test the FSM
	testInputs = ["IRSens"]
	# construct and initialise FSM
	ts = MonitorFSM()
	ts.start()
	ts.state = "activated"
	# display start state
	print('Start state:', ts.state)
	# display all state transitions prompted by
	# the specified list of test inputs
	for total_state in ts.transduce(testInputs):
		# display input, output, next state
		print(('In: {0[0]:<20s}'+
			  ' Out: {0[1]:<10s}'+
			  ' Next state: {0[2]:<10s}')
			  .format(total_state))	


def main():
	correct_code_sequence()
	incorrect_code_sequence()
	correct_code_for_deactivating()
	incorrect_code_for_deactivating()
	take_pic_test()

if __name__ == '__main__':
	main()