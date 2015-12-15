# IR_door_alarm
CM2540 Programming embedded devices coursework:                        Property surveillance system


Pierpaolo Lucraelli
1400571


Project Description
A suite of three Python programs that run on a Raspberry Pi for a simple property surveillance system.
































TABLE OF CONTENTS



STATEMENT OF COMPLIANCE…………………………………………………………...1
	Major software scripts……………………………………………………………….1.1
Required files. ………………………………………………………………………1.2

DESIGN DISCUSSION. ……………………………………………………………………...2

TEST PLAN AND RESULTS. ……………………………………………………………….3
	Purpose of the test. ………………………………………………………………….3.1
	Expected output. …………………………………………………………………….3.2
	Actual output. ……………………………………………………………………….3.3

































1. STATEMENT OF COMPLIANCE

1.	Program 1 – Activity monitor
1.1.	Activation with 4-digit code
1.2.	Appropriate response to movement (sensor trigger)
1.3.	Take picture
1.4.	Send Email
1.5.	Send Tweet
1.6.	Deactivation with 4-digit code
1.7.	GUI


All parts of the program have been successfully implemented and tested.


2.	Program 2 – Flask Server
2.1.	Run Server
2.2.	Gather images from static image folder
2.3.	Display images from the day in HTML page


All parts of the program have been successfully implemented and tested (see section 3 for tests)


3.	Program 3 – Administrator GUI
3.1.	Run activity monitor (Program 1)
3.2.	Kill activity monitor (Program 1)
3.3.	Run Flask server (Program 2)
3.4.	Kill Flask server (Program 2)
3.5.	Delete all Captured images
3.6.	GUI


All parts of the program have been successfully implemented and tested. (see section 3 for tests)













2. DESIGN DISCUSSION


Program 1 – Activity Monitor 


STATE DIAGRAM













2.2. REQUIRED FILES

The Activity monitor program is a Finite State Machine, having 5 different states:

•	deactivated
•	deactivated in transition
•	deactivated Transiting
•	activated
•	activated Transiting

It consists of 6 Python scripts:

•	FSM.py
•	MonitorFSM.py
•	main.py
•	camera.py
•	DrawShapes.py
•	SendData.py

This software requires the following hardware to run:
•	Raspberry Pi 
•	SenseHat (AstroPi)
•	PIR sensor
•	Webcam

The PIR sensor will be connected to the following pins of the Raspberry PI 

•	Vcc – PIN 2
•	Gnd – PIN 34
•	Out – PIN 33

As described by the state diagram, the machine has an initial state of “deactivated”.
During this state the SenseHat 8x8 led matrix will show a red cross.

The machine will pass to the next state (deactivated in transition) when machine receives user input, and return to “deactivated” if input is incorrect at any time.

In this state the led matrix will display a right arrow in red.
The function to test the code sequence (check_code()) is used both for activation and deactivation of the FSM.








check_code() function:




When correct code is entered The FSM will transition into the “deactivating transiting” state, and will remain in this state for a variable amount of time depending on the SLEEPTIME constant in main.py, then the FSM state will change to “activated”.
Change value of SLEEPTIME for a longer sleep time.
Default: 5 seconds.

To delay the activation, the function .after() is called on the GUI root window. 



When in the activated state, the PIR sensor becomes active and when movement is detected, the following actions will run.
•	Capture an image from the camera and save it as “[date-time].jpg” (camera.py – take_pic() )
•	Update the status of the twitter account (SendData.py – send_Tweet())
•	Send an email to email account (SendData.py – send_email())

Credentials for the Twitter and email are stored in the directory:
“./activity_monitor/credentials”, in separate “.txt” files.

main.py imports custom Python modules SendData.py for sending Tweets and Emails, and camera.py for taking pictures.

Script to change the shapes drawn on the SenseHat LED matrix is in the file DrawShapes.py




Program 2 – Flask server

Modules imported:

•	flask
•	os
•	Markup
•	datetime

Simple flask server running on port 5000 on local host.

This server will display all images captured by the camera from program 1 on a local web page.

To show images the <img> and <p> tags were created in Python script, then converted to Markup.


the <img> tags are sent to the the index.html template and rendered with the Jinja2 “{{ }}” function.



Program 3 – Administrator GUI

This program is used to control and run the other programs.
Basic GUI that can run / kill the activity monitor and the flask server.




Child calls were made using subprocess.Popen() to solve this problem.

All child processes are stored in a process group to make sure that when killing the child process all sub processed are terminated with it.

Delete images: For deleting the images a file list is created from the directory: (./flaskServer/static/camera), then files are deleted using the remove(file) method from the ‘os’ module.


Code for calling and killing the server process:











TEST PLAN AND RESULTS	

Purpose of the test:

Test for verifying the functionality of the activation with 4-digit code.
A list of inputs was fed into the FSM and according to the input, the correct output should have been displayed.

The test is divided into 5 parts:
•	Correct 4-digit sequence for activating FSM
•	Incorrect 4-digit sequence for activating FSM
•	Correct 4-digit sequence for deactivating FSM
•	Incorrect 4-digit sequence for deactivating FSM
•	Movement detected from sensor whilst activated

Expected output:

Part1 – state goes from deactivated to deactivate-in-trans – LED matrix:  Red circle
Part2 – state stays deactivated –LED matrix: Red cross
Part3 – state goes from activated to deactivated – LED matrix: Red cross
Part4 - state stays activated – LED matrix: Green circle
Part5 – state is alarmed – LED matrix: Green circle

Actual output:



Purpose of the test:

Testing if the processes have effectively been killed by the administrator panel.

List of running processes is shown in the LX terminal using:

Ps ax | grep python

After killing the processes with the admin panel, the same terminal command should show no python processes running.

No processes running initially, except for administrator.py



Activity monitor is called from admin panel (main.py)




Activity monitor is killed from admin panel (main.py)



Flask server is called from admin panel (server.py)



Flask server is killed from admin panel (server.py)


