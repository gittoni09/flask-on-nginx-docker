#!/usr/bin/python
import os
import socket
from datetime import datetime
from flask import Flask, render_template, request, jsonify
#Imports for MatPlotLib page
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#Constants
pathToPlot = './static'
imgPrefix = 'mathplot'
imgSuffix = '.png'

#Cleanup temp image directory
#folder = pathToPlot
#for the_file in os.listdir(folder):
#    file_path = os.path.join(folder, the_file)
#    try:
#        if os.path.isfile(file_path):
#            os.unlink(file_path)
#    except Exception as e:
#        print(e)

#Obtain hostname, if it exists 
try:
    hostname = socket.gethostname()
except:
    hostname = "No hostname"

#Define Flask app
app = Flask(__name__)
   
#Define all paths
@app.route('/')
def index():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    remote_addr = request.environ['REMOTE_ADDR']
    return render_template('index.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )

@app.route('/c2f')
def c2f():
    celsiusList = []
    farenList = []
    for cel in range(-20,101,10):
        celsiusList.append(cel) 
        faren = ((cel/5)*9)+32
        farenList.append(faren)
        cel =+ 10
    zipped = zip(celsiusList, farenList)
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    return render_template('c2f.html', x=zipped, hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )

@app.route('/f2c')
def f2c():
    celsiusList = []
    farenList = []
    for faren in range(-20,221,10):
        farenList.append(faren) 
        celsi = (((faren-32)*5)/9)
        celsiusList.append(celsi)
        faren =+ 10
    zipped = zip(farenList, celsiusList)
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    return render_template('f2c.html', x=zipped, hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )

@app.route('/guesser')
def guesser():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    return render_template('guesser.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )
	
@app.route('/missing')
def missing():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    return render_template('missing.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )

@app.route('/missingposition')
def missingpos():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    return render_template('missingpos.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )

@app.route('/wipeout')
def wipeout():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    return render_template('wipeout.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP )
	
@app.route('/matplot', methods=['POST', 'GET'])
def matplot():
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    imagepath = pathToPlot
    #Generate random name for image name based on current time to avoid cache issues
    midImgName = currentdatetime.strftime("%H%M%S%f")
    if request.method == 'POST':
        #Read and convert plot values
        xValues = request.form['xvalues'].split(',')
        xValuesInt = []
        for num in xValues:
            xValuesInt.append( int(num))
        yValues = request.form['yvalues'].split(',')
        yValuesInt = []
        for num in yValues:
            yValuesInt.append( int(num))
	#Line color combobox
        lineColor = request.form['color'] + "--"
        plt.plot (xValuesInt, yValuesInt, lineColor)
	#Read and conver axis values
        axisDef = (request.form['xaxis'] + ',' + request.form['yaxis']).split(',')
        axisDefInt = []
        for num in axisDef:
            axisDefInt.append( int(num))
        plt.axis (axisDefInt)
        #Save  and close plot
        imagepath = imagepath + '/' + imgPrefix + midImgName + imgSuffix
        plt.savefig (imagepath)
        plt.close ()
    webimagepath = imgPrefix + midImgName + imgSuffix
    return render_template('matplot.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP, webimagepath=webimagepath )

@app.errorhandler(404)
def not_found(error):
    currentdatetime = datetime.now()
    clientIP = request.remote_addr
    return render_template('error404.html', hostname=hostname, currentdatetime=currentdatetime, clientIP=clientIP ), 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


