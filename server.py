''' 
Author : Pierpaolo Lucarelli 
Flask app which will serve images captured from activity monitor
'''
from flask import Flask
from flask import render_template
import os
from flask import Markup
import datetime


app = Flask(__name__)

@app.route("/")
def index():

	fileNames = os.listdir("./static/camera")

	display = ""

	for i in range(0,len(fileNames)):
		
		display += "<div class = 'images'>\n"
		display += "<img src='./static/camera/%s'>\n" % fileNames[i]
		display += "<p>%s</p>\n" % fileNames[i][0:19]
		display += "</div>\n"

	if (display == ""):
		display = "<h1>No images to show</h1>"
	
	return render_template("index.html", images = Markup(display))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)
