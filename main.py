import json

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from datetime import timedelta

from chat import bot

app = Flask(__name__)
app.secret_key = "helloMynameisJohnWick"
app.permanent_session_lifetime = timedelta(days=7)


def admin(idx):
    with open('users.json', "r") as f:
        data = json.load(f)
    print(data[idx])
    print(data[idx]['admin'])
    return data[idx]['admin']


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method =="POST":
        usernm = request.form['username']
        pwd = request.form['password']
        admin = request.form['decision']
        if usernm == "":
            flash("Must complete the forms", "error")
            return redirect(url_for('signup'))
        else:
            if pwd == request.form['password2']:
                with open('users.json', "r") as f:
                    data = json.load(f)
                taken = False
                for _user in range(0, len(data)):
                    if data[_user]['username'] == usernm:
                        taken = True
                        flash("Username is taken, try different username", "error")
                        return redirect(url_for('signup'))

                #if taken == False:

                _dict = {'username':usernm, "password":pwd, "admin":admin}
                data.append(_dict)
                with open('users.json', 'w') as f:
                    json.dump(data,f, indent=4)
                session.permanent = True
                session['user_id'] = [usernm, admin]
                return redirect(url_for('chatbot'))
                #else:
                    #return redirect(url_for('signup'))
            else:
                flash("Incorrect password", "error")
                return redirect(url_for('signup'))
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
            with open('users.json') as f:
                data = json.load(f)
            user =[]
            idx = 0
            info = False
            for _user in range(0, len(data)):

                if data[_user]['username'] == usernm:
                    info = True
                    idx = _user
                    user=(data[_user]['username'])

            if info == False:
                flash("Incorrect username", "error")
                return redirect(url_for('login'))
            # user = [x for x in users if x.username == usernm][0]
            elif user and data[idx]['password'] == pwd:
                session.permanent=True
                session['user_id']=[user,admin(idx)]
                print(session['user_id'][1])


                return redirect(url_for('chatbot'))
            flash("Incorrect password", "error")
            return redirect(url_for('login'))
    return render_template('login.html')



@app.route('/chat', methods=["GET", "POST"])
def chatbot():

    if 'user_id' in session:

        user = session['user_id'][0]
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
@app.route("/admin", methods=['Post', 'GET'])
def admin_power():
    if request.method == 'POST':
        if request.form['admin'] == "Delete Users":
            return redirect(url_for('delete_users'))
    return render_template('admin.html')

@app.route("/deleteusers", methods=['Post', 'GET'])
def delete_users():
    return render_template('delete.html')
if __name__ == "__main__":
    app.run( debug=True)