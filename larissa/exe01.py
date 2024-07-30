from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return "Oiiiiiii"

@app.route('/curriculo')
def curriculo():
    return render_template("curriculo.html")

app.run(debug=True)
