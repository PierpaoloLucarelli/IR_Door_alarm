import picamera
import datetime
import os



def take_pic():

	
	filename = str(datetime.datetime.now()) + '.jpg'

	camera = picamera.PiCamera()

	camera.vflip = True

	try:
		print("taking picture")
		os.chdir("../flaskServer/static/camera")
		camera.capture(filename)
	finally:
		camera.close()
		os.chdir("../../../activity_monitor")
	print('Image captured')

