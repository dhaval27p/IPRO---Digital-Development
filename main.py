from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from datetime import timedelta

from chat import bot

app = Flask(__name__)
app.secret_key = "helloMynameisJohnWick"
app.permanent_session_lifetime = timedelta(days=7)



class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {repr(self.username)}>'

users =[]

users.append(User(id=1, username='Raj', password= '123'))
users.append(User(id=2, username='Dhaval', password= '1234'))
users.append(User(id=1, username='Rutvik', password= '123'))
users.append(User(id=2, username='Ciya', password= 'Inciya'))
print(users)



@app.route("/")
def home():
    return render_template("home.html")
@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method =="POST":
        usernm = request.form['username']
        pwd = request.form['password']

    return render_template("signup.html")
@app.route("/login", methods=['Post', 'GET'])
def login():
    if "user_id" in session:
        flash("Already Logged In!")
        return redirect(url_for('home'))

    if request.method =="POST":
        if request.form.get('Sign_up')=='Create User':
            return redirect(url_for("signup"))
        else:
            usernm = request.form['username']
            pwd = request.form['password']

            user = [x for x in users if x.username == usernm][0]
            if user and user.password == pwd:
                session.permanent=True
                session['user_id']=user.username

                return redirect(url_for('chatbot'))
            flash("Incorrect password", "error")
            return redirect(url_for('login'))
    return render_template('login.html')



@app.route('/chat', methods=["GET", "POST"])
def chatbot():

    if 'user_id' in session:

        user = session['user_id']
        if request.method == 'POST':
            the_question = request.form['question']
            response = bot(the_question)
            return jsonify({"response": response })
        else:
            return render_template('demo.html', user=user)
    else:
        flash("You are not logged in", "Warning")
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    if 'user_id' in session:
        user = session['user_id']
        flash("You have been logout!", "info")
    session.pop("user_id", None)
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run( debug=True)