from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe, hush hush!'

import random               #importing random number
import time                 #time.strftime("%Y/%m/%d %I:%M %p")
message = []

@app.route('/')
def index():
    if "totalgold" not in session:
        session['totalgold'] = 0
    return render_template('index.html', message=message)


@app.route('/process_money', methods=["POST"])
def process_money():

    if request.form['building'] == 'farm':                  #using insert to append activities to the top. Reverse append.
        gold = random.randint(10, 21)
        session['totalgold'] += gold
        message.insert(0, ("Earned " + str(gold) + " golds from the farm! " + time.strftime("(%Y/%m/%d %I:%M %p)")))

    elif request.form['building'] == 'cave':
        gold = random.randint(5, 10)
        session['totalgold'] += gold
        message.insert(0, ("Earned " + str(gold) + " golds from the cave! " + time.strftime("(%Y/%m/%d %I:%M %p)")))

    elif request.form['building'] == 'house':
        gold = random.randint(2, 5)
        session['totalgold'] += gold
        message.insert(0, ("Earned " + str(gold) + " golds from the house! " + time.strftime("(%Y/%m/%d %I:%M %p)")))

    elif request.form['building'] == 'casino':
        gold = random.randint(-50, 50)
        session['totalgold'] += gold
        if gold > 0:
            message.insert(0, ("Earned " + str(gold) + " golds from the casino! " + time.strftime("(%Y/%m/%d %I:%M %p)")))
        else:
            message.insert(0, ("Entered a casino and lost " + str(gold) + " golds...Yikers... " + time.strftime("(%Y/%m/%d %I:%M %p)")))

    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()                     #clears the total gold
    for i in message:                  #clears the message box
        message.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)