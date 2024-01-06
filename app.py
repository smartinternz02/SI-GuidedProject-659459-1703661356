from flask import *

app = Flask(__name__)

@app.route("/") # https://127.0.0.1:5000/
def home():
	return render_template("home.html")

@app.route("/calculate")
def calculate():
	return render_template("calculate.html")

@app.route("/book") 
def book():
	return render_template("book.html")

@app.route("/login") 
def login():
	return render_template("login.html")

@app.route("/register") 
def register():
	return render_template("register.html")

@app.route("/loggedin", methods=['post']) 
def loggedin():
	email=request.form['email']
	password=request.form['password']
	if email=='admin@gmail.com' and password=='1234':
		return render_template("home.html", user= email)
	elif email=='admin@gmail.com':
		return render_template("login.html", user="Wrong password! Enter the correct password.")
	else:
		return render_template("register.html", response="Wrong credentials. Kindly create an account.")


@app.route("/result", methods=['post']) 
def result():
	Vehicle=request.form['vehicle']
	if Vehicle == 'train':
		return render_template("result.html", response="According to the the European Environment Agency report (EEA), approximately 14g of CO2/passenger/km for the train.")
	elif Vehicle == 'car':
		return render_template("result.html", response="According to the the European Environment Agency report (EEA), approximately 42g to 55g of CO2/passenger/km for the car.")
	elif Vehicle == 'bus':
		return render_template("result.html", response="According to the the European Environment Agency report (EEA), approximately 68g of CO2/passenger/km for the bus.")
	elif Vehicle == 'bike':
		return render_template("result.html", response="According to the the European Environment Agency report (EEA), approximately 72g of CO2/passenger/km for the bike.")
	elif Vehicle == 'plane':
		return render_template("result.html", response="According to the the European Environment Agency report (EEA), approximately 285g of CO2/passenger/km for the plane.")


if __name__ == "__main__":
	app.run(debug=False, port=5000)