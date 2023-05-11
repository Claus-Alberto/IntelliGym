from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register/")
def register_screen():
    return render_template('register.html')

@app.route("/main/")
def main():
    return render_template('main.html', values = {
        'week': {
            'SEG':'check',
            'TER':'check',
            'QUA':'undone',
            'QUI':'check',
            'SEX':'check',
            'SAB':'uncheck',
            'DOM':'uncheck'
        },
        'training_name':'Pernas',
        'training': {
            'Leg Press' : {
                'Rep' : '15',
                'Series' : '4',
                'Peso' : '250'
            },
            'Agachamento Livre' : {
                'Rep' : '12',
                'Series' : '4',
                'Peso' : '80'
            },
            'Cadeira Extensora Unilateral' : {
                'Rep' : '12',
                'Series' : '4',
                'Peso' : '40'
            }
        }
    })

@app.route("/training/")
def training():
    return render_template('training.html')

if __name__ == '__main__':
    app.run(debug=True)
