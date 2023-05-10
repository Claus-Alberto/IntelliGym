from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register/")
def register_screen():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)