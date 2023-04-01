from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/register', methods = ['POST'])
def register():
    received_json = request.json

    # Exemplo de JSON
    # {
    #     "nomeCompleto": "",
    #     "email": "",
    #     "senha": "",
    #     "endereco": "",
    #     "cep": "",
    #     "numero": "",
    #     "telefone": "",
    #     "dataNascimento": "",
    #     "CPF": ""
    # }

    # Tratamento aqui
    
    response_json = {
        'success' : 'Aluno criado com sucesso'
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 201, 
        mimetype = 'application/json'
    )

@app.route('/get_aluno', methods = ['POST'])
def get_aluno():
    received_json = request.json

    # Exemplo de JSON
    # {
    #     'id' : 'id do aluno aqui'
    # }

    # Tratamento aqui
    
    response_json = {
        'nomeCompleto' : 'Claus Alberto Bienemann',
        'email' : 'claus.teste@teste.com',
        'endereco' : 'Rua dos Bobos',
        'cep' : '00000000',
        'numero' : '0',
        'telefone' : '(11) 9 9999-9999',
        'dataNascimento' : '11/11/1111',
        'CPF' : '123.456.789-98'
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 200, 
        mimetype = 'application/json'
    )

@app.route('/register_gym', methods = ['POST'])
def register_gym():
    received_json = request.json

    # Exemplo de JSON
    # {
    #     "nome": "",
    #     "email": "",
    #     "endereco": "",
    #     "senha": "",
    #     "cnpj": ""
    # }

    # Tratamento aqui
    
    response_json = {
        'success' : 'Academia criado com sucesso'
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 201, 
        mimetype = 'application/json'
    )

@app.route('/get_gym', methods = ['POST'])
def get_gym():
    received_json = request.json

    # Exemplo de JSON
    # {
    #     "id" : "id da academia aqui"
    # }

    # Tratamento aqui
    
    response_json = {
        "nome": "L7 Life Club",
        "email": "l7.teste@teste.com",
        "endereco": "Rua Dos Bobos, 0",
        "cnpj": "51.664.074/0001-63"
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 200, 
        mimetype = 'application/json'
    )

@app.route('/get_matricula', methods = ['POST'])
def get_matricula():
    received_json = request.json

    # Exemplo de JSON
    # {
    #     "idAluno" : "id do aluno",
    #     "idAcademia" : "id da Academia"
    # }

    # Tratamento aqui
    
    response_json = {
        "academiaId": "22bb11aa",
        "usuarioId": "11aa22bb",
        "ativa": True,
        "mensalidade": 209.00
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 200, 
        mimetype = 'application/json'
    )

@app.route('/get_dados_corporais', methods = ['POST'])
def get_dados_corporais():
    received_json = request.json

    # Exemplo de JSON
    # {
    #     "idAluno" : "id do aluno"
    # }

    # Tratamento aqui
    
    response_json = {
        "pesoAtual": 0,
        "altura": 0.0,
        "imc": 0.0,
        "percentualGordura": 0.0,
        "percentualMassaMuscular": 0.0,
        "aguaCorporal": 0.0,
        "metabolismoBasal": 0,
        "ingestaoCaloricaRec": 0,
        "pgc": 0.0
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 200, 
        mimetype = 'application/json'
    )

@app.route('/set_dados_corporais', methods = ['POST'])
def set_dados_corporais():
    received_json = request.json

    # Exemplo de JSON
    # {
        # "pesoAtual": 0,
        # "altura": 0.0,
        # "imc": 0.0,
        # "percentualGordura": 0.0,
        # "percentualMassaMuscular": 0.0,
        # "aguaCorporal": 0.0,
        # "metabolismoBasal": 0,
        # "ingestaoCaloricaRec": 0,
        # "pgc": 0.0,
        # "idAluno": ""
    # }

    # Tratamento aqui
    
    response_json = {
        'success' : 'Dado corporal criado com sucesso'
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 201, 
        mimetype = 'application/json'
    )

@app.route('/get_objetivo', methods = ['POST'])
def get_objetivo():
    received_json = request.json

    # Exemplo de JSON
    # {
    #     'idAluno' : 'id do aluno'
    # }

    # Tratamento aqui
    
    response_json = {
        "pesoDesejado": 0,
        "aguaCorporal": 0,
        "percentualMassaMuscular": 0.0,
        "percentualGordura": 0.0
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 200, 
        mimetype = 'application/json'
    )

@app.route('/set_objetivo', methods = ['POST'])
def set_objetivo():
    received_json = request.json

    # Exemplo de JSON
    # {
        # "pesoDesejado": 0,
        # "aguaCorporal": 0,
        # "percentualMassaMuscular": 0.0,
        # "percentualGordura": 0.0
        # idAluno: ''
    # }

    # Tratamento aqui
    
    response_json = {
        'success' : 'Objetivo criado com sucesso'
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 201, 
        mimetype = 'application/json'
    )

@app.route('/get_ficha', methods = ['POST'])
def get_ficha():
    received_json = request.json

    # Exemplo de JSON
    # {
    #     "idAluno" : "id do aluno"
    # }

    # Tratamento aqui
    
    response_json = {
        "dataInicial": 0,
        "dataFinal": 0,
        "divisoes": 0,
        "exercicios": ['Execícios aqui']
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 200, 
        mimetype = 'application/json'
    )

@app.route('/set_ficha', methods = ['POST'])
def set_ficha():
    received_json = request.json

    # Exemplo de JSON
    # {
    #    "dataInicial": 0,
    #    "dataFinal": 0,
    #    "divisoes": 0,
    #    "exercicios": ['Execícios aqui']
    #    idAluno: ''
    #    idTreinador: ''
    # }

    # Tratamento aqui
    
    response_json = {
        'success' : 'Ficha criada com sucesso'
    }
    
    return Response(
        json.dumps(response_json, indent = 4), 
        status = 201, 
        mimetype = 'application/json'
    )

if (__name__ == '__main__'):
    app.run(debug = True)
