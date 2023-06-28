from flask import Flask,render_template,request,flash,message_flashed
import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database ="tonstoys"
)

mycursor = mydb.cursor() 


app= Flask(__name__)

@app.route('/')
def index():
	return render_template('/index.html')

@app.route('/login')
def login():
	return render_template('/login.html')

@app.route('/contact')
def contact():
	return render_template('/contact.html')

@app.route('/signup')
def signup():
	return render_template('/signup.html')

@app.route('/submit-signup', methods=['post'])
def button_form():
	fname = request.form['firname']
	sname = request.form['secname']
	email = request.form['email']
	number = request.form['number']
	crpassword = request.form['crpassword']
	copassword = request.form['copassword']

	if(crpassword == copassword):
		query="INSERT INTO signup (fname,lname,email,number,crpassword) VALUES(%s,%s,%s,%s,%s) "
		data = (fname,sname,email,number,crpassword)
		mycursor.execute(query,data)
		mydb.commit()
		mycursor.close()
		mydb.close()
		return render_template('login.html')
	
	else:
		return render_template("signup.html", msg="different password")

@app.route('/submit-login', methods=['get'])
def loginform():
	email = request.args.get('email')
	crpassword = request.args.get('crpassword')
	query = "SELECT crpassword from signup WHERE email = %s"
	data = [email]
	'group-5'
	mycursor.execute(query,data)
	dpass = mycursor.fetchone()
	if(dpass is not None):
		d2pass = dpass[0]
		if(crpassword == d2pass):
			return render_template('index.html')

		else:
			return render_template('login.html',msg = "invalid username")	




		


if (__name__ == "__main__"):
	 app.run(debug = 'True')




