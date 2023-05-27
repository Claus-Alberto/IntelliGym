from flask import Flask, render_template, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import json

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'monstro'  # chave secreta para a geração de token JWT
jwt = JWTManager(app)

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

@app.route("/target/")
def target():
    return render_template('target.html')

@app.route("/profile/")
def profile():
    return render_template('profile.html')

@app.route("/progress/")
def progress():
    return render_template('commingsoon.html')

@app.route('/api/v1/login', methods=['POST'])
def login():
    access_token = create_access_token(identity='username')
    return jsonify({'access_token': access_token})

@app.route('/api/v2/treino', methods=['GET'])
@jwt_required()  # decora a rota com @jwt_required para exigir autenticação
def protected():
    data = {
        'grupoMuscular': [
            {'id': 1, 'nome': 'Costas'},
            {'id': 2, 'nome': 'Bíceps'},
            {'id': 3, 'nome': 'Tríceps'}
        ],
        'exercicios': [
            {'id': 1, 'nome': 'Pull Down', 'grupo': 1},
            {'id': 2, 'nome': 'Rosca Martelo', 'grupo': 2},
            {'id': 3, 'nome': 'Supino', 'grupo': 3}
        ],
        'exercicioTreino': [
            {'id': 1, 'exercicio': 1, 'repeticao': 10, 'peso': 20, 'series': 3},
            {'id': 2, 'exercicio': 2, 'repeticao': 12, 'peso': 15, 'series': 4},
            {'id': 3, 'exercicio': 3, 'repeticao': 8, 'peso': 30, 'series': 5}
        ],
        'treinoDiario': [
            {'id': 1, 'dia': '2023-05-12', 'executado': 1, 'exercicio': 1},
            {'id': 2, 'dia': '2023-05-12', 'executado': 1, 'exercicio': 2},
            {'id': 3, 'dia': '2023-05-12', 'executado': 0, 'exercicio': 3}
        ],
        'treino': [
            {'treinoDiario': 1, 'dataInicio': '2023-05-10', 'dataFim': '2023-05-15', 'aluno': 1},
            {'treinoDiario': 2, 'dataInicio': '2023-05-10', 'dataFim': '2023-05-15', 'aluno': 1},
            {'treinoDiario': 3, 'dataInicio': '2023-05-10', 'dataFim': '2023-05-15', 'aluno': 2}
        ]
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
