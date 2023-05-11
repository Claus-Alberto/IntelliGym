from crudDB import SQLiteCRUD 

def get_treino(id, date):
    columns = '''treino.dataInicio, treino.dataFim, treinoDiario.dia, treinoDiario.executado, 
            exercicioTreino.repeticao, exercicioTreino.peso, exercicioTreino.series, 
            exercicios.nome AS nome_exercicio, grupoMuscular.nome AS nome_grupoMuscular'''
    where = f'id = {id} AND treinoDiario.dia = {date}'
    join = '''JOIN treinoDiario ON treino.treinoDiario = treinoDiario.id
            JOIN exercicioTreino ON treinoDiario.exercicio = exercicioTreino.id
            JOIN exercicios ON exercicioTreino.exercicio = exercicios.id
            JOIN grupoMuscular ON exercicios.grupo = grupoMuscular.id
            '''
    db = SQLiteCRUD("IntellyGym.db")
    result = db.select('treino', columns, where, join)
    
    return result

def get_user_info(id):
    db = SQLiteCRUD("IntellyGym.db")
    result = db.select('aluno')
