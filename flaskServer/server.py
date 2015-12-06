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
		if(fileNames[i][0:11] == str(datetime.datetime.now())[0:11]):

			display += "<div class = 'images'>\n"
			display += "<img src='./static/camera/%s'>\n" % fileNames[i]
			display += "<p>%s</p>\n" % fileNames[i][0:19]
			display += "</div>\n"

	
	return render_template("index.html", images = Markup(display))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
