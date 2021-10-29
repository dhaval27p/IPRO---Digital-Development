from flask import Flask, render_template, request, jsonify
from chat import bot

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/chat', methods=["GET", "POST"])
def chatbot():
    if request.method == 'POST':
        the_question = request.form['question']
        response = bot(the_question)
        return jsonify({"response": response })
    else:
        return render_template('demo.html')


if __name__ == "__main__":
    app.run(debug=True)