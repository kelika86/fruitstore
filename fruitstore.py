from flask import Flask, render_template, request, redirect, session
app= Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    print(request)
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['strawberry']=request.form['strawberry']
    session['apple']=request.form['apple']
    session['rasberry']=request.form['rasberry']
    session['name']=request.form['name']
    session['number']=request.form['number']
    return redirect('/checkout')

@app.route('/checkout')
def checkout():
    return render_template("checkout.html")


app.run(debug=True)