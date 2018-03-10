from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
@app.route('/') #This is the root
def index():
	if 'serverNum' not in session:
		session['serverNum'] = random.randint(1,100)
	if 'guessIs' not in session:
		session['guessIs'] = 'start'
	return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
	serverNum = session['serverNum']
	userNum = int(request.form['guess'])
	if userNum == serverNum:
		session['guessIs'] = 'win'
		print "win"
	if userNum > serverNum:
		session['guessIs'] = 'high'
		print "high"
	if userNum < serverNum:
		session['guessIs'] = 'low'
		print "low"
	return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
	session['serverNum'] = random.randint(1,100)
	session['guessIs'] = 'start'
	return redirect('/')

app.run(debug=True)