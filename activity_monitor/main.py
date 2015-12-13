''' 
Author : Pierpaolo Lucarelli 
This class consists of a GUI for the Activity Monitor and handles the I/O of the activity monitor
'''

from tkinter import *
from MonitorFSM import *
#import custom made class for drawing shapes on the sensehat
import DrawShapes as DRAW
import time
import camera as CAM
try:
	import RPi.GPIO as GPIO
except RuntimeError:
		print('Error importing RPi.GPIO!\n',
			  'This is probably because you need superuser privileges.\n',
			  'You can achieve this by using "sudo" to run your script')
import SendData as SEND


# GUI initliazied with a lable 
class GUI(Tk):

	SLEEPTIME = 5000 #change to desired milliseconds
	IRSENSOR = 33 # IR sensor on pin 33

	def __init__(self):
		super().__init__()
		
		self.geometry('300x200')
		self.configure(background="black")
		self.title("Activity monitor")
		#header label
		self.header = Label(self, text = "IR sensor alarm", fg = "red" ,background='black')
		self.header.pack()
		#state label
		self.state_label = Label(self, text = "DEACTIVATED", fg = "red", background='black',font=("Helvetica", 16))
		self.state_label.pack(pady=(70,0))
		#state message label
		self.message_label = Label(self, text = "", fg = "red", background='black',font=("Helvetica", 16))
		self.message_label.pack()

		#binfing the <KeyPress> event to the GUI
		self.bind('<KeyPress>', self._onKeyPress) # if any key is pressed call _onKeyPress


		# use P1 header pin numbering convention
		GPIO.setmode(GPIO.BOARD)

		# configure pin 33 as input
		GPIO.setup(GUI.IRSENSOR, GPIO.IN)

		#call _IRSensorEvevt when ir signal recieved        
		GPIO.add_event_detect(GUI.IRSENSOR, GPIO.RISING, callback=self._IRSensorEvent)

		# create instance of monitor FSM and initialize to deactivated
		self.fsm = MonitorFSM()
		self.fsm.start()
		# draw a cross for the inital deactivated state
		DRAW._drawCross()



	#key pressed event 
	def _onKeyPress(self, event):
		if self.fsm.state != "deactivated-in-trans":
			# print(event.keysym)
			output = self.fsm.step(event.keysym)
			# print (output)
			self._process(output);

	#code to respond to movement detected form PIR sensor
	def _IRSensorEvent(self, channel):
		if self.fsm.state == "activated" or self.fsm.state == "activated-trans":
			print (self.fsm.state)
			output = self.fsm.step("IRSens")
			self._process(output)



	# from given output call the correct response
	def _process(self, output):
		#response to red cross output
		if output == "cross":
			DRAW._drawCross()
			self.state_label.configure(text="DEACTIVATED", fg="red")
			self.message_label.configure(text="", fg="red")
		#resposne to red right arrow output
		elif output == "right_arrow":
			DRAW._draw_rigth_arrow()
			self.state_label.configure(text="DEACTIVATED:")
			self.message_label.configure(text="> waiting for user input...")
		#response to left green arrow output
		elif output == "left_arrow":
			DRAW._draw_left_arrow()
			self.state_label.configure(text="ACTIVATED:")
			self.message_label.configure(text="> Waiting for user input...")
		#response to empty red circle output
		elif output == "empty_circle_red":
			self.state_label.configure(text="DEACTIVATED:")
			self.message_label.configure(text="Monitor will become active\n in {} seconds.".format(GUI.SLEEPTIME/1000))
			DRAW._draw_empty_circle()
			#used .after to avoid the freezing of the GUI
			self.after(GUI.SLEEPTIME, DRAW._draw_full_circle)
			self.after(GUI.SLEEPTIME, self.change_to_activated)
		elif output == "full_circle_green":
			DRAW._draw_full_circle()
			self.state_label.configure(text="ACTIVATED")
			self.message_label.configure(text="")
			# print(self.fsm.state)
		elif output == "alarmed":
			SEND.sendEmail()
			SEND.sendTweet()
			CAM.take_pic()


	def change_to_activated(self):
		self.state_label.configure(text = "ACTIVATED", fg = "green")
		self.message_label.configure(text="", fg = "green")
		self.fsm.state = "activated"

		

if __name__ == '__main__':
	app = GUI()
	app.mainloop()
	GPIO.cleanup()