from flask import Flask, render_template, request, flash

app = Flask(__name__,template_folder="template")
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
if __name__=="__main__":
	#app.run(debug=True)
	app.run(debug=False,host='0.0.0.0')