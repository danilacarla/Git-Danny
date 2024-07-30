from flask import flask, jsonify, request

app = Flask (__name__)

livros = [
    {
     
      'id' : 1,
      'livro' : 'lindo e cheiroso' ,
      'autor' : 'danny frança'
    },
    {
      'id' : 2,
       'livro' : 'Anakin Skywalker',
       'autor' : 'brito sem'

    },
    {
        'id' : 3,
        'livro' : 'miauu',
        'autor' : 'sophia rodrigues'
    },
]
@app . route ('/usuarios', methods=['GET'])
def consultar_usuarios ():
    return jsonify (usuarios)
    
@app . route ('/usuarios', methods=['GET'])
def consultar_usuarios_por_id(id):
    for usuario in usuarios:
        if usuario.get ('id') == id:
            return jsonify (usuario)

@app . route ('/usuarios', methods=['POST'])   
def consultar_usuario():
      novo_usuario = request.get_json()   
      usuarios.append (novo_usuario)  
      return jsonify (usuarios)

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro_por_id(id):
    if not request.is_json:
        return jsonify({'message': 'Tipo de mídia não suportado. Envie JSON.'})
    
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro_por_id(id):
    global livros
    livros = [livro for livro in livros if livro['id'] != id]
    if len(livros) == len(livros):
        return jsonify({'message': 'Livro não encontrado'}), 404
    return jsonify({'message': 'Livro excluído'}), 200


app.run(port=8080,host='localhost',debug=true)