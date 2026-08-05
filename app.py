from flask import Flask, render_template, request , redirect , url_for

app = Flask(__name__)

@app.route('/')
def home_form():
    return render_template('home.html')
@app.route('/' , methods = ['POST'] )
def home_submit():
    return redirect(url_for('cal_form'))

@app.route('/cal')
def cal_form():
    return render_template('calculator.html')

@app.route('/cal' , methods = ['POST'])
def cal_submit():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    operator = request.form['operator']

    if operator=="+" :
        answer = number1 + number2       
    elif operator=="-":
        answer = number1 - number2
    elif operator=="*":
        answer = number1 * number2
    elif operator=="/":
        answer = number1 / number2
    else :
       return f"please enter the correct operator use this only + , - , * , /  , as we don't support the coplex operators stil thanks!"

    return render_template('product.html' , result=answer)

if __name__ == '__main__':
    app.run(debug=True)
               
