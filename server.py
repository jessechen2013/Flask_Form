from flask import Flask, render_template, session, request, redirect, url_for,flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,10}')
app = Flask(__name__)
app.secret_key = 'youngOG'

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/check', methods=['POST'])
def validate():
	email = request.form['email']
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	password = request.form['password']
	password_confirm = request.form['password_confirm']
	

	if len(email) < 1 or len(firstname) < 1 or len(lastname) < 1 or len(password) < 1 or len(password_confirm) < 1:
		flash("All fields are required and must not be blank")
		return redirect('/')
		# just pass a string to the flash function
	elif not EMAIL_REGEX.match(email):
		flash("Invalid Email Address")
		return redirect('/')
	elif any(char.isdigit() for char in firstname + lastname):
		flash("Names must not contain any numbers")
		return redirect('/')
	elif not PASS_REGEX.match(password):
		flash("Password must be longer than 8 and shorter than 10 characters; with at least one number and uppercase letter")
		return redirect('/')
	elif password != password_confirm:
		flash("Please make sure password confirmation is same as the password")
		return redirect('/')
	return render_template('result.html', email=email, firstname = firstname, lastname = lastname)

@app.route('/reload', methods=['POST'])
def reload():
	return render_template('index.html')
app.run(debug=True)